import pytest
from flask import Request, Response

from src.controller.controller_csv import ControllerCsv
from src.exception.RequestFileException import RequestFileException


def test_controller_csv_request_file_except_error(request_test: Request, response_test: Response) -> None:
    with pytest.raises(RequestFileException) as rf:
        ControllerCsv.pdf_tables_to_csv_files_zipped(response_test, request_test)

    assert rf.value.args[0] == "file not found"
    assert rf.value.code == 404
