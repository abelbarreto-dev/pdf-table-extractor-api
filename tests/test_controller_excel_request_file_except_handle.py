import pytest
from flask import Request, Response

from src.controller.controller_excel import ControllerExcel
from src.exception.RequestFileException import RequestFileException


def test_controller_excel_request_file_except_error(request_test: Request, response_test: Response) -> None:
    with pytest.raises(RequestFileException) as rf:
        ControllerExcel.pdf_tables_to_excel_file(response_test, request_test)

    assert rf.value.args[0] == "file not found"
    assert rf.value.code == 404
