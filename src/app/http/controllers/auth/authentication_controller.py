
from fastapi import Depends, status, HTTPException

from app.http.dependencies.repositories import get_user_repository, get_refresh_token_repository
from app.repositories.refresh_token_repository import RefreshTokenRepository
from app.repositories.user_repository import UserRepository
from app.schemas.auth import LoginRequest, TokenResponse
from app.services.auth.token_service import TokenService
from app.services.authenticate_user_service import AuthenticateUserService


def login(
    payload: LoginRequest,
    user_repository: UserRepository = Depends(get_user_repository),
    refresh_token_repository: RefreshTokenRepository = Depends(get_refresh_token_repository)
) -> TokenResponse:
  service = AuthenticateUserService(
    user_repository=user_repository,
    refresh_token_repository=refresh_token_repository,
    token_service=TokenService()
  )

  try:
    tokens = service.execute(payload.email, payload.password)
  except ValueError:
    raise HTTPException(
      status_code=status.HTTP_401_UNAUTHORIZED,
      detail="Invalid credentials."
    )

  return TokenResponse(**tokens)