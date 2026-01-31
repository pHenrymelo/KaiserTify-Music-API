from dataclasses import dataclass
from uuid import UUID, uuid4

from app.domain.role import Role
from app.domain.value_objects.email import Email
from app.domain.value_objects.username import Username


@dataclass
class User:
  id: UUID
  username: Username
  email: Email
  hashed_password: str
  role: Role

  def __post_init__(self) -> None:


    if not isinstance(self.role, Role):
      raise ValueError("Invalid role")

  @classmethod
  def create(
          cls,
          username: Username,
          email: Email,
          hashed_password:str,
          role: Role
  ) -> "User":
    return cls(
      id=uuid4(),
      username=username,
      email=email,
      hashed_password=hashed_password,
      role=role
    )

  def is_artist(self):
    return self.role == Role.ARTIST

  def is_listener(self):
    return self.role == Role.LISTENER

