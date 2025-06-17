from flask import Response
from werkzeug.datastructures import FileStorage

from src.controller.controller_excel import ControllerExcel
from tests.mocks.request_test_factory import create_test_request


def test_controller_pdf_tables_to_excel_file_success(
        response_test: Response,
        pdf_file: FileStorage
) -> None:
    request_pdf = create_test_request(pdf_file)

    result = ControllerExcel.pdf_tables_to_excel_file(response_test, request_pdf)

    assert result.status_code == 201
    assert result.content_type == "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
