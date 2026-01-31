
from fastapi import Depends, status, HTTPException

from app.http.controllers.dependencies.repositories import get_user_repository
from app.repositories.user_repository import UserRepository
from app.schemas.auth import LoginRequest, TokenResponse
from app.services.auth.token_service import TokenService
from app.services.authenticate_user_service import AuthenticateUserService


def login(
    payload: LoginRequest,
    user_repository: UserRepository = Depends(get_user_repository)
):
  auth_service = AuthenticateUserService(user_repository)
  token_service = TokenService()

  try:
    user = auth_service.execute(payload.email, payload.password)
    token = token_service.create_access_token(user)
  except ValueError:
    raise HTTPException(
      status_code = status.HTTP_401_UNAUTHORIZED,
      detail="Invalid credentials."
    )

  return TokenResponse(access_token=token)