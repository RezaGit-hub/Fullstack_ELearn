from datetime import datetime
from uuid import UUID

from pydantic import BaseModel, EmailStr, Field, field_validator
from app.core.camelbase import _CamelBase

#Basic
class UserBase(BaseModel):
    email: EmailStr

    @field_validator("email", mode="after")
    @classmethod
    def _normalize_email(cls, v:str) -> str:
        return v.lower().strip()                       #email auf lowercase + whitespace

# Eingehen: Singup
class UserCreate(UserBase):
    password: str = Field(
        min_length=8, max_length=72,
        description="geben Sie bitte Mindestens 8 Zeichen. Bcrypt-limit 72 Bytes. ",
    )
    @field_validator("password", mode="after")
    @classmethod
    def _check_password_strength(cls, v: str) -> str:
        if not any(c.isdigit() for c in v):
            raise ValueError("Password muss mindestens eine Zahl enthalten")
        return v

#Ausgehend: Response
class UserRead(UserBase, _CamelBase):
    id : UUID
    is_active: bool
    is_superuser: bool
    created_at: datetime


#Eingehend: Login-Body
class UserLogin(BaseModel):
    email: EmailStr
    password: str


#Einghend: Patch
class UserUpdate(_CamelBase):
    is_active: bool | None = None
    is_superuser: bool | None = None