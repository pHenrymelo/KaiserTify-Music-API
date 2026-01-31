from dataclasses import dataclass

@dataclass(frozen=True)
class Email:
  value: str

  def __post_init__(self) -> None:
    if not self.value or "@" not in self.value:
      raise ValueError("Invalid email")