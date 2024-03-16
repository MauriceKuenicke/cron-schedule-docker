import logging
import sys
import os
from dotenv import load_dotenv
load_dotenv()

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s %(levelname)-8s %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    stream=sys.stdout
)

if __name__ == "__main__":
    foo_env, bar_env = os.getenv("VAR1", None), os.getenv("VAR2", None)

    if not all([foo_env, bar_env]):
        logging.error("Error during load of environment variables.")
        quit()

    logging.info("Cron schedule alive.")
