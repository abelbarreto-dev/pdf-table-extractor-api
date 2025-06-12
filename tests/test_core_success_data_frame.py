from werkzeug.datastructures import FileStorage

from src.core.data_frame.data_frame import get_data_frame
from tests.mocks.table_data_frame import data_frame_fruits, data_frame_teams


def test_core_success_data_frame(pdf_file: FileStorage) -> None:
    expect_data = (data_frame_fruits, data_frame_teams)
    response_data = get_data_frame(pdf_file)

    assert len(response_data) == len(expect_data)
    assert all(df1.equals(df2) for df1, df2 in zip(response_data, expect_data))
