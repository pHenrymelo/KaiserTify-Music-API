from uuid import UUID

from pydantic import BaseModel, EmailStr

from app.domain.role import Role
from app.domain.value_objects.email import Email


class RegisterUserRequest(BaseModel):
  username: str
  email: EmailStr
  password: str
  role: Role

class UserResponse(BaseModel):
  id: UUID
  username: str
  email: Email
  role: Role

class LoginRequest(BaseModel):
  email: EmailStr
  password: str

class TokenResponse(BaseModel):
  access_token: str
  token_type: str = "bearer"