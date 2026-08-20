from datetime import datetime

from uuid import UUID , uuid4
from sqlalchemy import Boolean, String, DateTime, func
from sqlalchemy.dialects.postgresql import UUID as PG_UUID
from sqlalchemy.orm import Mapped, mapped_column

from app.db.base import Base

class User(Base):
    __tablename__= "user"

    id : Mapped[UUID]= mapped_column(
        PG_UUID(as_uuid=True),
        primary_key=True,
        default=uuid4,
    )

    email: Mapped[str] = mapped_column(
        String(255), nullable=False, unique=True, index=True,
    )

    password_hash: Mapped[str]= mapped_column(
        String(255), nullable=False, 
    )

    is_active: Mapped[bool]= mapped_column(
        Boolean, nullable=False, default=True, server_default="true",
    )

    is_superuser: Mapped[bool]= mapped_column(
        Boolean, nullable=False, default=False, server_default="false",
    )

    created_at: Mapped[datetime]= mapped_column(
        DateTime(timezone=True), server_default=func.now(), nullable=False,
    )

    update_at: Mapped[datetime]= mapped_column(
        DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False,
    )


    def __repr__(self) -> str:
        return f"<User id={self.id} email={self.email}>"