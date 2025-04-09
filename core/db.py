import asyncpg
import asyncio


class Database:
    _instance = None
    _pool = None

    def __new__(cls):
        """Ensuring only one instance of Database exists."""
        if cls._instance is None:
            cls._instance = super(Database, cls).__new__(cls)
        return cls._instance

    async def init_pool(self, database, user, password, host, port, min_size=1, max_size=5):
        """Initializing the connection pool once."""
        if self._pool is None:
            self._pool = await asyncpg.create_pool(
                database=database,
                user=user,
                password=password,
                host=host,
                port=port,
                min_size=min_size,
                max_size=max_size
            )

    async def fetch(self, query, *args):
        """Fetch data from the database."""
        async with self._pool.acquire() as connection:
            return await connection.fetch(query, *args)

    async def execute(self, query, *args):
        """Execute a database query"""
        async with self._pool.acquire() as connection:
            return await connection.execute(query, *args)

    async def executemany(self, query, args_list):
        """Execute the same query multiple times with different parameters in a single transaction."""
        async with self._pool.acquire() as connection:
            async with connection.transaction():
                await connection.executemany(query, args_list)

    async def close_pool(self):
        """Close the database connection pool"""
        if self._pool:
            await self._pool.close()
            self._pool = None
