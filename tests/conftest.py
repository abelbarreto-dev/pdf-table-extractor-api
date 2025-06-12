from os.path import isfile
from typing import Generator

import pytest
from werkzeug.datastructures import FileStorage


@pytest.fixture(scope="function")
def file_none() -> Generator[FileStorage, None]:
    yield FileStorage(content_type="application/pdf")


@pytest.fixture(scope="function")
def pdf_file() -> Generator[FileStorage, None]:
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
