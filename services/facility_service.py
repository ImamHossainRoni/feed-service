from core.base_service import Service
from core.db import Database
from daos.facility_dao import FacilityDao


class FacilityService(Service):
    dao_cls = FacilityDao

    async def get_all_facilities(self):
        """Fetch all facilities using DAO"""
        return await self.dao.get_all()

    async def insert_facilities(self, facility_data: list[list]):
        await self.dao.save_batch(facility_data)
