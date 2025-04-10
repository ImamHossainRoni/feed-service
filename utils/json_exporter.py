import json
import os
import gzip
import time
from pathlib import Path
from settings import Settings


class JSONExporter:
    def __init__(self, service, output_dir="output", page_size=100):
        self.service = service
        self.output_dir = output_dir
        self.page_size = page_size
        self.generated_files = []
        self.output_dir = os.path.join(Settings.BASE_DIR, output_dir)
        Path(self.output_dir).mkdir(parents=True, exist_ok=True)

    async def export_paginated(self):
        page = 1
        while True:
            offset = (page - 1) * self.page_size
            records = await self.service.dao.get_paginated(limit=self.page_size, offset=offset)

            if not records:
                break

            expected_data = self._format_data(records)
            filename = self._write_to_gzipped_json_file(page, expected_data)
            self.generated_files.append(filename)
            print(f"page = {page}")
            page += 1
            self._write_metadata_file()

    @staticmethod
    def _format_data(records):
        """Format the records into the desired structure."""
        expected_json_data = {
            "data": [
                {
                    "entity_id": record.get("entity_id"),
                    "name": record.get("name"),
                    "telephone": record.get("telephone"),
                    "url": record.get("url"),
                    "location": {
                        "latitude": record.get("latitude"),
                        "longitude": record.get("longitude"),
                        "address": {
                            "country": record.get("country"),
                            "locality": record.get("locality"),
                            "region": record.get("region"),
                            "postal_code": record.get("postal_code"),
                            "street_address": record.get("street_address")
                        }
                    }
                }
                for record in records
            ]
        }
        return expected_json_data

    def _write_to_gzipped_json_file(self, page, records):
        timestamp = int(time.time_ns())
        filename = f"facility_feed_{timestamp}.json.gz"
        file_path = os.path.join(self.output_dir, filename)

        with open(file_path, "wt", encoding="utf-8") as gz_file:
            json.dump(records, gz_file, indent=2, default=str)

        print(f"Page {page} is converted to gzipped json and location is: {file_path}")

        return filename

    def _write_metadata_file(self):
        metadata = {
            "generation_timestamp": int(time.time()),
            "name": "reservewithgoogle.entity",
            "data_file": self.generated_files
        }

        metadata_path = os.path.join(self.output_dir, "metadata.json")
        with open(metadata_path, 'w', encoding='utf-8') as f:
            json.dump(metadata, f, indent=2)

    def _upload_to_s3(self):
        pass
