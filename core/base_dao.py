
"""
This module implements the  DAO pattern.
Reference:
    - https://medium.com/@devcorner/dao-design-pattern-the-complete-guide-f8246f227091
    - https://stackoverflow.com/questions/69677507/data-access-object-dao-in-python-flask-sqlalchemy
Data Access Object (DAO) pattern for database interaction.
"""
from abc import ABC, abstractmethod

import asyncpg

from core.db import Database


class Dao(ABC):
    def __init__(self, db: Database = None):
        """Initializing with a Database instance"""
        self.db = db

    @abstractmethod
    def table_name(self):
        """Table name must be defined in subclasses"""
        pass

    @property
    def columns(self):
        pass

    async def get_all(self):
        """Fetch all records from the table"""
        query = f"SELECT * FROM {self.table_name};"
        return await self.db.fetch(query)

    async def save_batch(self, rows: list[list], batch_size: int = 1000):
        """Insert multiple rows"""
        if not rows:
            return Exception("Rows must have value!")
        placeholders = ", ".join([f"${i + 1}" for i in range(len(self.columns))])
        query = f"""
                INSERT INTO {self.table_name} ({', '.join(self.columns)})
                VALUES ({placeholders})
                """

        for i in range(0, len(rows), batch_size):
            batch = rows[i:i + batch_size]
            # print(batch)
            try:
                await self.db.executemany(query, batch)
            except asyncpg.exceptions.StringDataRightTruncationError as e:
                print(e)
                print(batch[i])




