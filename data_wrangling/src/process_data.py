"""
Process data
"""

import logging.config
import pandas as pd
import yaml

from datetime import datetime


def main_function(config, logger):
    """ Main function """
    logger.info("Main function")

    # Read input data
    a_df = pd.read_csv(**config["input"]["a"])
    b_df = pd.read_excel(**config["input"]["b"])

    # Data exploration
    logger.debug(a_df.shape)
    logger.debug(b_df.shape)

    logger.debug(a_df.head())
    logger.debug(b_df.head())

    # Data processing
    # ...

    # Export results
    a_df.to_csv(**config["output"]["a"])
    b_df.to_csv(**config["output"]["b"])

    logger.info("Script finished")


if __name__ == "__main__":
    config = yaml.safe_load(open("process_data.yml"))

    config["logs"]["handlers"]["file"]["filename"] = datetime.now().strftime(
        config["logs"]["handlers"]["file"]["filename"]
    )
    logging.config.dictConfig(config["logs"])
    logger = logging.getLogger(__name__)

    try:
        main_function(config, logger)
    except Exception:
        logger.exception("Exception occurred", exc_info=True)
