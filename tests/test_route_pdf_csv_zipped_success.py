from flask.testing import FlaskClient
from werkzeug.datastructures import FileStorage

from tests.mocks.envs_test_enum import EnvsTestEnum


def test_route_pdf_csv_zipped_success(
        app_test: FlaskClient,
        pdf_file: FileStorage
) -> None:
    data = {"file": (pdf_file.stream, pdf_file.filename, "application/pdf")}

    response = app_test.post(
        "/pdf-csv",
        data=data,
        content_type=EnvsTestEnum.CONTENT_TYPE.value
    )

    assert response
    assert response.status_code == 201
