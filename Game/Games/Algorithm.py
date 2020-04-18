from abc import ABC, abstractmethod


class Algorithm(ABC):


    @abstractmethod
    def calculate_score(self):
        pass



    @abstractmethod
    def get_align_result(self) -> list:
        pass

    @abstractmethod
    def get_score(self) -> int:
        pass

    @abstractmethod
    def get_input_alignments(self) -> list:
        pass

    @abstractmethod
    def get_input_panalty(self) -> list:
        pass
