from flask import Blueprint, make_response, send_file, Response, request

from src.controller.controller_csv import ControllerCsv
from src.wrapper.exception_hanlder import exception_handler

pdf_csv = Blueprint("csv-routes", __name__, url_prefix="/pdf-csv")


@pdf_csv.post("")
@exception_handler
def take_tables_pdf_to_csv_zipped():
    resp = ControllerCsv.pdf_tables_to_csv_files_zipped(Response(), request)

    excel = resp.stream
    excel.seek(0)

    response = make_response(send_file(
        excel,
        mimetype=resp.mimetype,
        as_attachment=True,
        download_name=resp.headers["filename-csv-zipped"]
    ))

    response.status_code = resp.status_code
    return response
