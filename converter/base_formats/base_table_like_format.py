from abc import ABC, abstractmethod


class BaseTableLikeFormat(ABC):
    format: str
    arguments: list

    def __init__(self, cli_arguments):
        self.skip = cli_arguments[0]
        self.take = cli_arguments[1]

    @abstractmethod
    def convert_from_string_to_array(self, data: str) -> list:
        pass
