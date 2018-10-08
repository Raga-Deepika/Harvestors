import logging



logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
logger.setLevel(logging.WARNING)
logger.setLevel(logging.ERROR)


logging.basicConfig(filename="entrepreneur.logs",level=logging.DEBUG, format='%(asctime)s:%(name)s:%(message)s')
