from os import remove
from os.path import isfile
from typing import List

from pandas import DataFrame
from tabula import read_pdf

from src.exception.FileNotFound import FileNotFound


def get_data_frame(pdf_file: str) -> List[DataFrame]:
    if not isfile(pdf_file):
        raise FileNotFound("pdf file not found")

    try:
        return read_pdf(pdf_file, pages="all")
    finally:
        remove(pdf_file)
