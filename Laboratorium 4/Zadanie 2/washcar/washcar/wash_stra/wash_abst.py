from abc import ABC, abstractmethod
from .program_lib import standard, premium


class AbstractWash(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def program(self, program_array):
        pass


class WashProgramStandard(AbstractWash):
    def __init__(self):
        super().__init__()

    def program(self, program_array):
        standard(program_array)


class WashProgramPremium(AbstractWash):
    def __init__(self):
        super().__init__()

    def program(self, program_array):
        premium(program_array)
