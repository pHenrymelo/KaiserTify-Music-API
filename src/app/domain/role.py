from enum import Enum

class Role(str, Enum):
  LISTENER = "listener"
  ARTIST = "artist"