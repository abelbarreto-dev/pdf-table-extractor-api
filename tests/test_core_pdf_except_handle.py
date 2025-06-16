import pytest
from werkzeug.datastructures import FileStorage

from src.core.data_frame.data_frame import get_data_frame
from src.exception.file_not_found_exception import FileNotFoundException
from src.exception.table_not_found_exception import TableNotFoundException


def test_core_pdf_not_found(file_none: FileStorage) -> None:
    with pytest.raises(FileNotFoundException) as ex:
        get_data_frame(file_none)

    assert ex.value.code == 404
    assert ex.value.args[0] == "pdf file not found"


def test_core_pdf_without_tables_exception(pdf_not_tables: FileStorage) -> None:
    with pytest.raises(TableNotFoundException) as ex:
        get_data_frame(pdf_not_tables)

    assert ex.value.code == 404
    assert ex.value.args[0] == "not one table found at that pdf file"
