import logging


def log_init():
    
    logger = logging.getLogger('Evaluation_Log')
    logger.setLevel(logging.INFO)
    formatter = logging.Formatter('%(asctime)s - %(module)s - %(levelname)s - %(message)s')
    fh = logging.FileHandler('eval.log')
    ch = logging.StreamHandler()
    fh.setFormatter(formatter)
    ch.setFormatter(formatter)
    logger.addHandler(fh)
    logger.addHandler(ch)

    logger.info('Logger initialized')
    


