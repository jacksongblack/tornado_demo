from core.model import Model
from sqlalchemy import Column, Integer, String


class User(Model):
    username = Column(String(length=300))
    password = Column(String(length=300))
    email = Column(String(length=500))


class Group(Model):
    name = Column(String(length=300))
