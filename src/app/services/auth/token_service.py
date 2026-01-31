from datetime import datetime, timedelta

from jose import jwt

from app.core.settings import settings
from app.domain.user import User


class TokenService:
  def create_access_token(self, user: User) -> str:
    payload = {
      "sub": str(user.id),
      "role": user.role.value,
      "exp": datetime.utcnow() + timedelta(minutes=30)
    }
    return jwt.encode(payload, settings.secret_key, algorithm="HS256")