from typing import List

from pandas import DataFrame
from tabula import read_pdf
from werkzeug.datastructures import FileStorage

from src.exception.FileNotFound import FileNotFound


def get_data_frame(pdf_file: FileStorage) -> List[DataFrame]:
    if not pdf_file:
        raise FileNotFound("pdf file not found")

    pdf_file.stream.seek(0)

    return read_pdf(pdf_file.stream, pages="all")
