__author__ = "github.com/AndrewSazonov"
__version__ = "0.0.1"

import os
import sys
import tempfile
import logging


class StreamToLogger(object):
   """
   Fake file-like stream object that redirects writes to a logger instance.
   """
   def __init__(self, logger, log_level):
      self.logger = logger
      self.log_level = log_level
      self.linebuf = ''

   def write(self, buf):
      for line in buf.rstrip().splitlines():
         self.logger.log(self.log_level, line.rstrip())

log_filepath = os.path.join(tempfile.gettempdir(), 'easydiffraction.log')
os.unlink(log_filepath)
print("Log file:", log_filepath)

logging.basicConfig(
    level=logging.WARNING,
    format='%(asctime)s %(levelname)8s %(name)-10s %(filename)-15s %(funcName)-20s %(lineno)4d %(message)s',
    filename=log_filepath,
    filemode="w"
)

stdout_logger = logging.getLogger('stdout')
sl = StreamToLogger(stdout_logger, logging.WARNING)
sys.stdout = sl

stderr_logger = logging.getLogger('stderr')
sl = StreamToLogger(stderr_logger, logging.ERROR)
sys.stderr = sl