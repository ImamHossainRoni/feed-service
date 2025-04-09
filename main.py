from settings import Settings
from core.db import Database
import asyncio
from services.facility_service import FacilityService
from utils import FakeDataGenerator


async def main():
    db = Database()

    db_config = Settings.DB_CONFIG
    await db.init_pool(**db_config)

    facility = FacilityService(db)

    fake_data_generator = FakeDataGenerator()
    facilities = fake_data_generator.generate_fake_facilities(3000)
    await facility.insert_facilities(facilities)

    facilities = await facility.get_all_facilities()
    # print(facilities)

    await db.close_pool()


if __name__ == "__main__":
    asyncio.run(main())
