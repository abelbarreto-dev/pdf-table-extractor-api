import pytest
from werkzeug.datastructures import FileStorage

from src.exception.file_not_found_exception import FileNotFoundException
from src.exception.table_not_found_exception import TableNotFoundException
from src.exception.type_file_exception import TypeFileException
from src.service.service_csv import ServiceCsv


def test_service_csv_mimetype_pdf_error(file_json: FileStorage) -> None:
    with pytest.raises(TypeFileException) as ex:
        ServiceCsv.get_csv_single_file(file_json)

    assert ex.value.code == 400
    assert ex.value.args[0] == "the file sent must be pdf format"


def test_service_csv_stream_file_null_error(file_none: FileStorage) -> None:
    with pytest.raises(FileNotFoundException) as ex:
        ServiceCsv.get_csv_single_file(file_none)

    assert ex.value.code == 400
    assert ex.value.args[0] == "file content can not be null"


def test_service_pdf_without_tables_error(pdf_not_tables) -> None:
    with pytest.raises(TableNotFoundException) as ex:
        ServiceCsv.get_csv_single_file(pdf_not_tables)

    assert ex.value.code == 404
    assert ex.value.args[0] == "not one table found at that pdf file"
