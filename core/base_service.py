"""
This module implements the  Service layer to separate business logic.
Reference:
    - https://breadcrumbscollector.tech/how-to-implement-a-service-layer-in-django-rest-framework/
    - https://sensidev.com/blog/django-service-layer/
"""

from abc import ABC, abstractmethod
from .base_dao import Dao
from .db import Database


class Service(ABC):
    def __init__(self, db: Database):
        self._db = db

    @property
    @abstractmethod
    def dao_cls(self) -> type:
        """Each service must define its DAO class"""
        pass

    @property
    def dao(self) -> Dao:
        """Return an instance of the DAO class with the database connection"""
        return self.dao_cls(self._db)
