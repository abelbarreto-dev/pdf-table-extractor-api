from io import BytesIO

from pandas import read_excel
from pandas.testing import assert_frame_equal
from werkzeug.datastructures import FileStorage

from src.service.service_excel import ServiceExcel


def test_service_excel_success(pdf_file: FileStorage, expect_excel_file_with_tabs: BytesIO) -> None:
    response_excel = ServiceExcel.get_excel_file(pdf_file)

    response_excel.seek(0)
    expect_excel_file_with_tabs.seek(0)

    excel_resp = read_excel(response_excel, sheet_name=None)
    excel_expect = read_excel(expect_excel_file_with_tabs, sheet_name=None)

    assert excel_resp.keys() == excel_expect.keys()

    for sheet_name in excel_resp.keys():
        assert_frame_equal(excel_resp[sheet_name], excel_expect[sheet_name])
