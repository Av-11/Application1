import logging
from lib.Logger import configure_logger  # This will configure the root logger for use
from lib.input.inputreader import InputReaderFactory
from lib.output.outputwriter import OutputWriterFactory


logger = logging.getLogger()


def main(input_file, db_type):
    # get input reader object
    reader = InputReaderFactory.get_reader(input_file)
    logger.debug("Selected reader [%s]" % reader)

    # get output writer object
    writer = OutputWriterFactory.get_writer(input_file)
    logger.debug("Selected reader [%s]" % writer)


if __name__ == '__main__':
    input_file = "employee.csv"
    db_type = "sqlite"
    main(input_file, db_type)