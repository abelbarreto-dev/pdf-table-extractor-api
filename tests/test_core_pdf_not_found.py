import pytest

from src.core.data_frame.data_frame import get_data_frame
from src.exception.FileNotFound import FileNotFound


def test_core_pdf_not_found() -> None:
    file = "/pdfs-tests/file-pdf-example.pdf"

    with pytest.raises(FileNotFound) as ex:
        get_data_frame(file)
        assert ex.value == "pdf file not found"
