import pytest

from fastapi.testclient import TestClient
from app.core.application import create_app

@pytest.fixture
def test_app():
  app = create_app(testing=True)
  return TestClient(app)