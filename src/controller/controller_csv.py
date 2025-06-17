from io import BytesIO

from flask import Response, Request
from werkzeug.datastructures import FileStorage

from src.exception.RequestFileException import RequestFileException
from src.service.service_csv import ServiceCsv
from src.util.compress_zip_util import compress_several_files_to_zip


class ControllerCsv:
    @classmethod
    def pdf_tables_to_csv_files_zipped(cls, response: Response, request: Request):
        if not request.files or "file" not in request.files.keys():
            raise RequestFileException()

        pdf_file = request.files["file"]

        csv_files = ServiceCsv.get_csv_single_file(pdf_file)
        format_csv = pdf_file.filename[: pdf_file.filename.index(".")]
        zip_file = format_csv + ".zip"
        format_csv += "_{}.csv"

        csv_files = tuple(csv for csv in csv_files)
        csv_count = len(csv_files)

        csv_map = map(
            lambda csv, i: (format_csv.format(i), BytesIO(csv.encode("utf-8"))),
            csv_files, range(csv_count)
        )

        csv_buffer = compress_several_files_to_zip(csv_map, zip_file)

        csv_resp = FileStorage(
            stream=csv_buffer,
            filename=zip_file,
            name=pdf_file.name
        )

        response.stream = csv_resp
        response.status_code = 201
        response.mimetype = "application/zip"

        return response
