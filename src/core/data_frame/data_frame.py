from typing import List

from pandas import DataFrame
from tabula import read_pdf
from werkzeug.datastructures import FileStorage

from src.exception.file_not_found_exception import FileNotFoundException
from src.exception.table_not_found_exception import TableNotFoundException


def get_data_frame(pdf_file: FileStorage) -> List[DataFrame]:
    if not pdf_file:
        raise FileNotFoundException("pdf file not found")

    pdf_file.stream.seek(0)

    pdf_tables = read_pdf(pdf_file.stream, pages="all")

    if not pdf_tables:
        raise TableNotFoundException("not one table found at that pdf file", 404)

    return pdf_tables
