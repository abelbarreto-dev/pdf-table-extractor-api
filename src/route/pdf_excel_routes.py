from flask import Blueprint, request, Response, make_response
from werkzeug.utils import send_file

from src.controller.controller_excel import ControllerExcel
from src.wrapper.exception_hanlder import exception_handler

pdf_excel = Blueprint("excel-routes", __name__, url_prefix="/pdf-excel")


@pdf_excel.post("")
@exception_handler
def take_tables_pdf_to_excel():
    resp = ControllerExcel.pdf_tables_to_excel_file(Response(), request)

    excel = resp.stream
    excel.seek(0)

    response = make_response(send_file(
        excel,
        mimetype=resp.mimetype,
        as_attachment=True,
        download_name=resp.headers["filename-excel"],
        environ=request.environ
    ))

    response.status_code = resp.status_code
    return response
