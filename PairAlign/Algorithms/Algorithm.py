from abc import ABC, abstractmethod


class Algorithm(ABC):
    """
    Abstract Class for PairAlign algorithm classes
    """

    @abstractmethod
    def initialize(self):
        """
        Initializes values for DP matrices
        """

    @abstractmethod
    def calculate_score(self):
        """
        Executes alignment algorithm
        """

    @abstractmethod
    def traceback(self):
        """
        Finds traceback path using score matrix and direction matrix
        """

    @abstractmethod
    def get_alignments(self) -> list:
        """
        Returns final alignment results
        """

    @abstractmethod
    def get_score(self) -> int:
        """
        Returns final score
        """

    @abstractmethod
    def get_score_matrix(self) -> int:
        """
        Returns DP score matrix
        """

    @abstractmethod
    def get_direction_matrix(self) -> int:
        """
        Returns the direction matrix which has the way each value was calculated
        """
