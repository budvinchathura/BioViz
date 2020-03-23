from abc import ABC, abstractmethod


class Algorithm(ABC):

    @abstractmethod
    def initialize(self):
        pass

    @abstractmethod
    def calculate_score(self):
        pass

    @abstractmethod
    def traceback(self):
        pass

    @abstractmethod
    def get_alignments(self) -> list:
        pass

    @abstractmethod
    def get_score(self) -> int:
        pass

    @abstractmethod
    def get_score_matrix(self) -> int:
        pass

    @abstractmethod
    def get_direction_matrix(self) -> int:
        pass

    @abstractmethod
    def get_identity(self) -> int:
        pass