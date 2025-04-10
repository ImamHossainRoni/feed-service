from settings import Settings
from core.db import Database
import asyncio
from services.facility_service import FacilityService
from utils import FakeDataGenerator
from utils.json_exporter import JSONExporter


async def main():
    db = Database()

    db_config = Settings.DB_CONFIG
    await db.init_pool(**db_config)

    facility = FacilityService(db)

    fake_data_generator = FakeDataGenerator()
    # facilities = fake_data_generator.generate_fake_facilities(1000)
    # await facility.insert_facilities(facilities)

    facilities = await facility.get_all_facilities()
    print(facilities)
    print(len(facilities))

    # page = 1
    # page_size = 100
    # offset = (page - 1) * page_size
    #
    # facilities = await facility.dao.get_paginated(limit=page_size, offset=offset)
    # print(facilities)
    # print(len(facilities))

    json_exporter = JSONExporter(facility, output_dir="output", page_size=100)
    await json_exporter.export_paginated()

    await db.close_pool()


if __name__ == "__main__":
    asyncio.run(main())
