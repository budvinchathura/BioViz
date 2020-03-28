from abc import ABC, abstractmethod

class Algorithm(ABC):

    @abstractmethod
    def align(self):
        pass

    def get_alignments(self) -> list:
        pass
