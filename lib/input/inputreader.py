import csv
import sys
import inspect
import logging

logger = logging.getLogger()


class InputReaderFactory:
    @staticmethod
    def get_reader(input_file):
        clsmembers = inspect.getmembers(sys.modules[__name__], inspect.isclass)
        ext = input_file.split(".")[-1]
        for member in clsmembers:
            if member[0] == 'InputReaderFactory':
                continue
            try:
                if member[1].get_type() == ext:
                    return member[1](input_file)
            except NotImplementedError:
                continue


class InputReader:
    """Interface to implement a reader class"""
    def read_row(self):
        raise NotImplementedError

    def read_rows(self):
        raise NotImplementedError

    @staticmethod
    def get_type(self):
        raise NotImplementedError

    def get_columns(self):
        raise NotImplementedError


class CsvInputReader(InputReader):
    def __init__(self, csv_file):
        self.csv_file = csv_file
        logger.info("Initializing csv reader for file [%s]" % self.csv_file)

    def get_columns(self):
        # 1st row of csv file will be treated as column names
        with open(self.csv_file, newline='') as csvfile:
            reader = csv.reader(csvfile, delimiter=' ', quotechar='|')

    def read_row(self):
        pass

    def read_rows(self, count=5):
        pass

    @staticmethod
    def get_type():
        return "csv"



