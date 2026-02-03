from fastapi import FastAPI
from app.http.controllers.health_controller import router as health_router
from app.http.controllers.auth.router import router as authentication_router
from app.http.controllers.users.router import router as users_router

def create_app() -> FastAPI:
  app = FastAPI(title="KaiserTify")

  app.include_router(health_router)
  app.include_router(authentication_router)
  app.include_router(users_router)

  return app