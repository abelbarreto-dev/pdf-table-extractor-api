from io import BytesIO
from typing import Any

from pandas import ExcelWriter
from werkzeug.datastructures import FileStorage

from src.core.data_frame.data_frame import get_data_frame
from src.exception.file_not_found_exception import FileNotFoundException
from src.exception.type_file_exception import TypeFileException


class ServiceExcel:
    @classmethod
    def get_excel_file(cls, pdf_file: FileStorage) -> Any:
        if pdf_file.mimetype != "application/pdf":
            raise TypeFileException("the file sent must be pdf format")

        if not pdf_file:
            raise FileNotFoundException("file content can not be null", 400)

        data_frames = get_data_frame(pdf_file)

        buffer = BytesIO()

        with ExcelWriter(buffer, engine="openpyxl") as writer: # type: ignore
            for i, df in enumerate(data_frames):
                df.to_excel(writer, sheet_name=f"Sheet_{i+1}", index=False)

        buffer.seek(0)
        return buffer
