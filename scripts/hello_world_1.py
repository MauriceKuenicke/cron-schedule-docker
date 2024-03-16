from common import return_a_string
import logging

logger = logging.getLogger(__name__)

if __name__ == "__main__":
    for i in range(10):
        my_str = return_a_string()
        logger.info("Running Hello World 1")
        print(my_str)

