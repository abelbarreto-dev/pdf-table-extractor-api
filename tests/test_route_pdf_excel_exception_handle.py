from flask.testing import FlaskClient
from werkzeug.datastructures import FileStorage

from tests.mocks.envs_test_enum import EnvsTestEnum


def test_route_pdf_excel_error(
        app_test: FlaskClient,
        pdf_file: FileStorage
) -> None:
    response = app_test.post(
        "/pdf-excel",
        data=None,
        content_type=EnvsTestEnum.CONTENT_TYPE.value
    )

    assert response
    assert response.status_code == 404
    assert response.data == b'{"error": "file not found"}'
