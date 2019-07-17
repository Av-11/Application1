import sys
import inspect
import logging

logger = logging.getLogger()


class OutputWriterFactory:
    @staticmethod
    def get_writer(input_file):
        clsmembers = inspect.getmembers(sys.modules[__name__], inspect.isclass)
        ext = input_file.split(".")[-1]
        for member in clsmembers:
            if member[0] == 'OutputWriterFactory':
                continue
            try:
                if member[1].get_type() == ext:
                    return member[1](input_file)
            except NotImplementedError:
                continue


class OutputWriter:
    def create_table(self):
        raise NotImplementedError

    def add_row(self):
        raise NotImplementedError

    @staticmethod
    def get_type():
        raise NotImplementedError


class SqliteOutputWriter(OutputWriter):
    def create_table(self):
        pass

    def add_row(self):
        pass

    @staticmethod
    def get_type():
        return "sqlite"


