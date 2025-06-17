from flask import Flask

from flask_cors import CORS

from src.route.pdf_csv_routes import pdf_csv
from src.route.pdf_excel_routes import pdf_excel


app = Flask(__name__)

resources = {
    r"*": {
        "origins": "*"
    }
}

CORS(app)
# CORS(app, resources=resources)

app.register_blueprint(pdf_csv)
app.register_blueprint(pdf_excel)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
