from abc import ABC, abstractmethod
from typing import TypeVar, Generic

T = TypeVar('T')

class Metric(ABC, Generic[T]):
    def __init__(self, sample_id: str) -> None:
        self.sample_id = sample_id

    @abstractmethod
    def value(self, metrics_dir: str) -> T:
        pass

    @abstractmethod
    def name(self) -> str:
        pass

