from abc import ABC, abstractmethod


class BaseHumanReadableFormat(ABC):
    format: str
    arguments: list

    def __init__(self, cli_arguments):
        self.skip = cli_arguments[0]
        self.take = cli_arguments[1]

    @abstractmethod
    def convert_from_array_to_string(self, array: list) -> str:
        pass
