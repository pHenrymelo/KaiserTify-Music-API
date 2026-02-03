from fastapi import APIRouter
from app.http.controllers.users.get_profile_controller import get_profile
from app.http.controllers.users.update_profile_controller import update_profile

router = APIRouter(prefix="/users", tags=["Users"])

router.get("/me")(get_profile)
router.put("/me")(update_profile)