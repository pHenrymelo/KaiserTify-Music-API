from fastapi import Depends, HTTPException, status

from app.domain.role import Role
from app.domain.user import User
from app.http.dependencies.security import get_current_user

def require_role(*allowed_roles: Role):
  def dependency(current_user: User = Depends(get_current_user)) -> User:
    if current_user.role not in allowed_roles:
      raise HTTPException(
        status_code=status.HTTP_403_FORBIDDEN,
        detail="Forbidden"
      )

    return current_user

  return dependency

def require_artist():
  return require_role(Role.ARTIST)

def require_listener():
  return require_role(Role.LISTENER)

def require_authenticated():
  return require_role(Role.LISTENER, Role.ARTIST)