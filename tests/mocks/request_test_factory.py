from flask import Request, Flask
from werkzeug.datastructures import FileStorage


def create_test_request(file: FileStorage = None) -> Request:
    app = Flask(__name__)
    app.config["TESTING"] = True

    files = {
        "file": (file.stream, file.filename, file.content_type)
    }

    with app.test_request_context(
        method="POST",
        data=files,
        content_type="multipart/form-data"
    ) as context:
        return context.request
