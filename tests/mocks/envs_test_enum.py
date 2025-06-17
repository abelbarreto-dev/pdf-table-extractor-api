from enum import Enum
from os import environ

from dotenv import load_dotenv


load_dotenv()


class EnvsTestEnum(Enum):
    BASE_URL=environ["TEST_BASE_URL"]
    PORT=int(environ["TEST_PORT"])
    CONTENT_TYPE=environ["TEST_CONTENT_TYPE"]
