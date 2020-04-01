from abc import ABC, abstractmethod

class Algorithm(ABC):
    """
    Abstract Class for MSA algorithm classes
    """

    @abstractmethod
    def initialize(self):
        """
        Initializes values for DP matrices
        """
    @abstractmethod
    def align(self):
        """
        Executes alignment algorithm
        """
    @abstractmethod
    def calculate_identity(self):
        """
        Calculates identity factor in final alignment
        """
    @abstractmethod
    def get_alignments(self) -> list:
        """
        Returns final alignment
        """
