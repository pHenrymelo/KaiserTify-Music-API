from fastapi import FastAPI
from app.http.controllers.health_controller import router as health_router
from app.http.controllers.auth.router import router as authentication_router

def create_app() -> FastAPI:
  app = FastAPI(title="KaiserTify")

  app.include_router(health_router)
  app.include_router(authentication_router)

  return app