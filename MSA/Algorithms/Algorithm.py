from abc import ABC, abstractmethod


class Algorithm(ABC):
    """
    Abstract Class for MSA algorithm classes
    """

    def __init__(self):
        self.alignments = []
        self.identity = 0

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

    def calculate_identity(self):
        """
        Calculates identity factor in final alignment
        """
        prof_n = len(self.alignments)
        len_algn = len(self.alignments[0])
        iden = 0
        for i in range(prof_n):
            for j in range(i+1, prof_n):
                for k in range(len_algn):
                    ch_1 = self.alignments[i][k]
                    ch_2 = self.alignments[j][k]
                    if ch_1 == ch_2:
                        iden += 1
        self.identity = 2 * iden / (len_algn * prof_n * (prof_n-1))

    @abstractmethod
    def get_alignments(self) -> list:
        """
        Returns final alignment
        """
