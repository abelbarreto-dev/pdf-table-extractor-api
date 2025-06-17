from flask import Response, Request
from werkzeug.datastructures import FileStorage

from src.exception.RequestFileException import RequestFileException
from src.service.service_excel import ServiceExcel


class ControllerExcel:
    @classmethod
    def pdf_tables_to_excel_file(cls, response: Response, request: Request):
        if not request.files or "file" not in request.files.keys():
            raise RequestFileException()

        pdf_file = request.files["file"]

        excel_file = ServiceExcel.get_excel_file(pdf_file)
        format_excel = pdf_file.filename[: pdf_file.filename.index(".")]
        format_excel += ".xlsx"

        excel = FileStorage(
            stream=excel_file,
            filename=format_excel,
            name=pdf_file.name
        )

        response.stream = excel
        response.status_code = 201
        response.mimetype = "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
        response.headers["filename-excel"] = format_excel

        return response
