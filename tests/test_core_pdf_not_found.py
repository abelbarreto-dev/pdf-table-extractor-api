import pytest
from werkzeug.datastructures import FileStorage

from src.core.data_frame.data_frame import get_data_frame
from src.exception.FileNotFound import FileNotFound


def test_core_pdf_not_found(file_none: FileStorage) -> None:
    with pytest.raises(FileNotFound) as ex:
        get_data_frame(file_none)

    assert ex.value.args[0] == "pdf file not found"
