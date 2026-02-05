from fastapi import FastAPI, Header

from app.core.openapi import configure_openapi
from app.http.controllers.health_controller import router as health_router
from app.http.controllers.auth.router import router as authentication_router
from app.http.controllers.users.router import router as users_router

def create_app() -> FastAPI:
  app = FastAPI(title="KaiserTify")

  app.include_router(health_router)
  app.include_router(authentication_router)
  app.include_router(users_router)

  configure_openapi(app)

  return app