import json
from abc import ABC

from converter.base_formats.base_human_readable_format import BaseHumanReadableFormat


class JSON(BaseHumanReadableFormat, ABC):
    def convert_from_array_to_string(self, array: list) -> str:
        title = array[0]
        data = array[1:]
        return json.dumps([dict(zip(title, data_row)) for data_row in data], indent=4)
