
"""
This module implements the  DAO pattern.
Reference:
    - https://medium.com/@devcorner/dao-design-pattern-the-complete-guide-f8246f227091
    - https://stackoverflow.com/questions/69677507/data-access-object-dao-in-python-flask-sqlalchemy
Data Access Object (DAO) pattern for database interaction.
"""
from abc import ABC, abstractmethod
from core.db import Database


class Dao(ABC):
    def __init__(self, db: Database = None):
        """Initializing with a Database instance"""
        self.db = db

    @abstractmethod
    def table_name(self):
        """Table name must be defined in subclasses"""
        pass

    async def get_all(self):
        """Fetch all records from the table"""
        query = f"SELECT * FROM {self.table_name};"
        return await self.db.fetch(query)


