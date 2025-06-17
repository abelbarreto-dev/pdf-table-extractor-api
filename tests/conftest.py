from io import BytesIO
from os.path import isfile
from typing import Generator

import pytest
from dotenv import load_dotenv
from flask import Response, Request, Flask
from flask.testing import FlaskClient
from pandas import ExcelWriter
from werkzeug.datastructures import FileStorage

from src.route.pdf_csv_routes import pdf_csv
from src.route.pdf_excel_routes import pdf_excel
from tests.mocks.table_data_frame import data_frame_teams, data_frame_fruits
from tests.mocks.envs_test_enum import EnvsTestEnum


load_dotenv()


@pytest.fixture(scope="function")
def file_none() -> Generator[FileStorage, None, None]:
    yield FileStorage(content_type="application/pdf")


@pytest.fixture(scope="function")
def file_json() -> Generator[FileStorage, None, None]:
    yield FileStorage(content_type="application/json")


@pytest.fixture(scope="function")
def pdf_file() -> Generator[FileStorage, None, None]:
    pdf = FileStorage(content_type="application/pdf")

    filename = (
        "file_test_pdf.pdf"
        if isfile("file_test_pdf.pdf")
        else "../file_test_pdf.pdf"
    )

    with open(filename, "rb") as doc:
        pdf.stream = doc
        pdf.filename = "file_test_pdf.pdf"
        pdf.name = "pdf of test"

        yield pdf


@pytest.fixture(scope="function")
def pdf_not_tables() -> Generator[FileStorage, None, None]:
    pdf = FileStorage(content_type="application/pdf")

    filename = (
        "file_test_not_tables.pdf"
        if isfile("file_test_not_tables.pdf")
        else "../file_test_not_tables.pdf"
    )

    with open(filename, "rb") as doc:
        pdf.stream = doc
        pdf.filename = "file_test_not_tables.pdf"
        pdf.name = "pdf of test not tables"

        yield pdf


@pytest.fixture(scope="function")
def expect_excel_file_with_tabs() -> Generator[BytesIO, None, None]:
    data_frames = (data_frame_fruits, data_frame_teams)

    buffer = BytesIO()

    with ExcelWriter(buffer, engine="openpyxl") as writer:  # type: ignore
        for i, df in enumerate(data_frames):
            df.to_excel(writer, sheet_name=f"Sheet_{i + 1}", index=False)

    buffer.seek(0)
    yield buffer



@pytest.fixture(scope="function")
def response_test() -> Generator[Response, None, None]:
    yield Response()


@pytest.fixture(scope="function")
def app_test() -> Generator[FlaskClient, None, None]:
    app = Flask(__name__)
    app.config["TESTING"] = True
    app.config["HOST"] = EnvsTestEnum.BASE_URL
    app.config["POST"] = EnvsTestEnum.PORT

    app.register_blueprint(pdf_csv)
    app.register_blueprint(pdf_excel)

    with FlaskClient(app) as client:
        yield client


@pytest.fixture(scope="function")
def request_test() -> Generator[Request, None, None]:
    app = Flask(__name__)
    app.config["TESTING"] = True

    with app.test_request_context() as context:
        yield context.request
