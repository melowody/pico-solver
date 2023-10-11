from abc import ABC, abstractmethod


class PicoSolver(ABC):

    @abstractmethod
    def get_name(self) -> str:
        pass

    @abstractmethod
    def get_description(self) -> str:
        pass

    @abstractmethod
    def solve(self) -> str:
        pass
