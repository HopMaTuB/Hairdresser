import enum
from datetime import date
from uuid import UUID, uuid4

from sqlalchemy import Integer, String, DateTime, func, Enum, ForeignKey, Column, Table
from sqlalchemy.dialects.postgresql import UUID as PGUUID
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship


class Base(DeclarativeBase):
	pass


class Role(enum.Enum):
	admin: str = "admin"
	moderator: str = "moderator"
	user: str = "user"


class User(Base):
	__tablename__ = 'users'
	
	id: Mapped[UUID] = mapped_column(PGUUID(as_uuid=True), primary_key=True, default=uuid4)
	username: Mapped[str] = mapped_column(String(50), unique=True, nullable=False)
	first_name: Mapped[str] = mapped_column(String(50), nullable=False)
	email: Mapped[str] = mapped_column(String(100), unique=True, nullable=False)
	password: Mapped[str] = mapped_column(String(255), nullable=False)
	created_at: Mapped[date] = mapped_column("created_at", DateTime, default=func.now())
	updated_at: Mapped[date] = mapped_column("updated_at", DateTime, default=func.now(), onupdate=func.now())
	role: Mapped[Role] = mapped_column("role", Enum(Role), default=Role.user)
	
	@property
	def is_admin(self):
		return self.role == Role.admin

	@property
	def is_moderator(self):
		return self.role == Role.moderator

class Client(Base):
	__tablename__ = 'clients'
	
	id: Mapped[UUID] = mapped_column(PGUUID(as_uuid=True), primary_key=True, default=uuid4)
	name: Mapped[str] = mapped_column(String(100), nullable=False,unique=True)
	phone: Mapped[str] = mapped_column(String(20), nullable=False)

class Record(Base):
	__tablename__ = 'records'

	id: Mapped[UUID] = mapped_column(PGUUID(as_uuid=True), primary_key=True, default=uuid4)
	client_id: Mapped[UUID] = mapped_column(UUID, relationship(Client.id),nullable=False)
	user_id: Mapped[UUID] = mapped_column(UUID,relationship(User.id),nullable=False)
	record_date: Mapped[DateTime] = mapped_column(DateTime, nullable=False)
	cost: Mapped[float] = mapped_column(float, nullable=False)