from abc import ABC, abstractmethod


class AbstractAttack(ABC):
    """
    une attaque
    """

    def __init__(self, power=0, name=None, description=None):
        self._power: int = power
        self._name: str = name
        self._description: str = description

    @abstractmethod
    def compute_damage(self) -> int:
        pass
