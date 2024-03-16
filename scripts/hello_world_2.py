from common import return_a_string
import logging
import sys

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s %(levelname)-8s %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    stream=sys.stdout
)

if __name__ == "__main__":
    for i in range(10):
        my_str = return_a_string()
        logging.info("Running Hello World 2")
        print(my_str)

