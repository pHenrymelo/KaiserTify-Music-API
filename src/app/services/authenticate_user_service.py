from app.domain.user import User
from app.core.security import verify_password
from app.domain.value_objects.email import Email
from app.repositories.user_repository import UserRepository


class AuthenticateUserService:
  def __init__(self, user_repository: UserRepository):
    self.user_repository = user_repository

  def execute(self, email: str, password: str) -> User:

    email_vo = Email(email)

    user = self.user_repository.get_by_email(email_vo)

    if not user:
      raise ValueError("Invalid Credentials")

    if not verify_password(password, user.hashed_password):
      raise ValueError("Invalid Credentials")

    return user