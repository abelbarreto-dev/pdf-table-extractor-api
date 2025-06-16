from werkzeug.datastructures import FileStorage

from src.service.service_csv import ServiceCsv
from tests.mocks.table_data_frame import data_frame_fruits, data_frame_teams


def test_service_single_csv_success(pdf_file: FileStorage) -> None:
    response_data = ServiceCsv.get_csv_single_file(pdf_file)

    response_data = tuple(df for df in response_data)

    expect_data = (
        data_frame_fruits.to_csv(index=False),
        data_frame_teams.to_csv(index=False)
    )

    assert len(response_data) == len(expect_data)
    assert all(df1 == df2 for df1, df2 in zip(response_data, expect_data))
