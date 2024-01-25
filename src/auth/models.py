from datetime import datetime

from fastapi_users_db_sqlalchemy import SQLAlchemyBaseUserTable
from sqlalchemy import Column, Integer, String, ForeignKey, Boolean, TIMESTAMP, MetaData, Table, JSON

from src.database import Base

metadata = MetaData()

role = Table(
    'role',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('name', String, nullable=False),
    Column('permissions', JSON)
)

user = Table(
    'user',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('email', String, unique=True, index=True, nullable=False),
    Column('username', String, nullable=False),
    Column('role_id', Integer, ForeignKey(role.c.id)),
    Column('hashed_password', String, nullable=False),
    Column('is_active', Boolean, default=True, nullable=False),
    Column('is_superuser', Boolean, default=False, nullable=False),
    Column('is_verified', Boolean, default=False, nullable=False),
    Column('last_enter', TIMESTAMP, default=datetime.utcnow())
)


class User(SQLAlchemyBaseUserTable[int], Base):
    id: int = Column(Integer, primary_key=True)
    email: str = Column(String(length=320), unique=True, index=True, nullable=False)
    username: str = Column(String(length=320), nullable=False)
    role_id: int = Column(Integer, ForeignKey(role.c.id))
    hashed_password: str = Column(String(length=1024), nullable=False)
    is_active: bool = Column(Boolean, default=True, nullable=False)
    is_superuser: bool = Column(Boolean, default=False, nullable=False)
    is_verified: bool = Column(Boolean, default=False, nullable=False)
    last_enter: datetime = Column(TIMESTAMP, default=datetime.utcnow)
