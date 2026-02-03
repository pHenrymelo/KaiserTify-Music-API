from app.domain.user import User
from app.repositories.user_repository import UserRepository

class DeleteUserService:
  def __init__(self, user_repository: UserRepository):
    self.user_repository = user_repository

  def execute(self, user: User):
    self.user_repository.delete(user)