import logging
import os


def configure_logger(log_file="application1.log"):
    if not os.path.exists(log_file):
        open(log_file, 'w+').close()

    print("Configuring logger %s" % log_file)
    # use the root logger
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)

    # configure log handlers
    fh = logging.FileHandler(log_file)
    fh.setLevel(logging.INFO)
    ch = logging.StreamHandler()
    ch.setLevel(logging.ERROR)

    # configure logging format
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    fh.setFormatter(formatter)
    ch.setFormatter(formatter)

    # add log handlers
    logger.addHandler(fh)
    logger.addHandler(ch)


# TODO make this configurable using a config file from UI
configure_logger()
