from fastapi import APIRouter

from app.http.controllers.auth.register_controller import register_user
from app.http.controllers.auth.authentication_controller import login
from app.schemas.auth import UserResponse, TokenResponse

router = APIRouter(prefix="/auth", tags=["Auth"])

router.post("/register", response_model=UserResponse, status_code=201)(register_user)
router.post("/session", response_model=TokenResponse, status_code=200)(login)