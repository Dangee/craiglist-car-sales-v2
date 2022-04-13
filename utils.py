"""
Utilities library
Define custom functions for main app
"""

import logging
import params as p

def configure_logging():
  logging.basicConfig(format='%(asctime)s - [%(levelname)s] (%(module)s:%(funcName)s:%(lineno)d) %(message)s')
  logger = logging.getLogger()
  try:
    logger.setLevel(p.LOG_LEVEL.upper())
  except AttributeError as error:
    logger.setLevel(logging.INFO)
    logger.warning(f"Using INFO level because {p.LOG_LEVEL.upper()} is not a valid level")
  return logger