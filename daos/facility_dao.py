from core.base_dao import Dao
from core.db import Database


class FacilityDao(Dao):
    table_name = 'facility'

    @property
    def columns(self):
        return [
            "name", "phone", "url", "latitude", "longitude",
            "country", "locality", "region", "postal_code", "street_address"
            ]


