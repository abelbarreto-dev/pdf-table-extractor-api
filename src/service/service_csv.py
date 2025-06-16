from typing import Generator

from werkzeug.datastructures import FileStorage

from src.core.data_frame.data_frame import get_data_frame
from src.exception.file_not_found_exception import FileNotFoundException
from src.exception.type_file_exception import TypeFileException


class ServiceCsv:
    @classmethod
    def get_csv_single_file(cls, pdf_file: FileStorage) -> Generator[str, None, None]:
        if pdf_file.mimetype != "application/pdf":
            raise TypeFileException("the file sent must be pdf format")

        if not pdf_file:
            raise FileNotFoundException("file content can not be null", 400)

        data_frames = get_data_frame(pdf_file)

        return (df.to_csv(index=False) for df in data_frames)
