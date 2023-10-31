import argparse
import sys
import importlib


class CLI:
    parser: argparse
    format: list
    skip: int
    take: int

    def __init__(self):
        self.parser = argparse.ArgumentParser(description='Converter')
        self.parser.add_argument('--format', dest='format', type=str, help='determine the type of conversion')
        self.parser.add_argument('--skip', dest='skip', type=int, help='determine how many items to skip')
        self.parser.add_argument('--take', dest='take', type=int, help='determine how many items to take')

    def run(self):
        args = self.parser.parse_args()
        self.format = args.format.split('_to_')
        self.skip = args.skip
        self.take = args.take
        arguments = [self.skip, self.take]
        table_like_module = importlib.import_module(f"converter.table_like_formats.{self.format[0]}")
        table_like_classname = str(self.format[0]).upper()
        table_like_class = getattr(table_like_module, table_like_classname)
        table_like_instance = table_like_class(cli_arguments=arguments)
        if not sys.stdin.isatty():
            table_like_array_data = table_like_instance.convert_from_string_to_array(data=sys.stdin)
            table_like_array_data_processed = table_like_instance.process_array(array=table_like_array_data)
            human_readable_module = importlib.import_module(f"converter.human_readable_formats.{self.format[1]}")
            human_readable_classname = str(self.format[1]).upper()
            human_readable_class = getattr(human_readable_module, human_readable_classname)
            human_readable_instance = human_readable_class(arguments)
            sys.stdout.write(human_readable_instance.convert_from_array_to_string(table_like_array_data_processed))
        else:
            raise OSError
