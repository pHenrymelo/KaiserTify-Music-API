from app.domain.user import User
from app.domain.value_objects.email import Email
from app.domain.value_objects.username import Username
from app.repositories.user_repository import UserRepository


class UpdateUserService:
  def __init__(self, user_repository: UserRepository):
    self.user_repository = user_repository

  def execute(
          self,
          user: User,
          username: str | None,
          email: str | None
  ) -> User:
    if username:
      user.change_username(Username(username))
    if email:
      user.change_email(Email(email))

    self.user_repository.save(user)
    return user