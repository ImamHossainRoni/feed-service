from settings import Settings
from core.db import Database
import asyncio
from services.facility_service import FacilityService


async def main():
    db = Database()

    db_config = Settings.DB_CONFIG
    await db.init_pool(**db_config)

    facility = FacilityService(db)
    facilities = await facility.get_all_facilities()
    print(facilities)

    await db.close_pool()


if __name__ == "__main__":
    asyncio.run(main())
