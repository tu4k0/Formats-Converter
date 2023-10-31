from abc import ABC

from converter.base_formats.base_table_like_format import BaseTableLikeFormat


class CSV(BaseTableLikeFormat, ABC):
    def convert_from_string_to_array(self, data: str) -> list:
        return [line.strip().split(',') for line in data]

    def process_array(self, array: list) -> list:
        return [array[0]] + array[self.skip + 1:self.skip + self.take + 1]
