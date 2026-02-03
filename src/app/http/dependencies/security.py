from uuid import UUID

from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt

from app.core.settings import settings
from app.http.dependencies.repositories import get_user_repository
from app.repositories.user_repository import UserRepository
from app.domain.user import User

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/session")

def get_current_user(
        token: str = Depends(oauth2_scheme),
        user_repository: UserRepository = Depends(get_user_repository)
) -> User:
  try:
    payload = jwt.decode(
      token,
      settings.secret_key,
      algorithms=["HS256"]
    )
    user_id: str | None = payload.get("sub")
    if not user_id:
      raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Invalid Token."
      )
  except JWTError:
    raise HTTPException(
      status_code=status.HTTP_401_UNAUTHORIZED,
      detail="Invalid Token."
    )

  user = user_repository.get_by_id(UUID(user_id))
  if not user:
    raise HTTPException(
      status_code=status.HTTP_401_UNAUTHORIZED,
      detail="User not found."
    )

  return user