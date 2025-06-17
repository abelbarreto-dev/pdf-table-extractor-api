from os import getenv

from flask import Flask
from flask.cli import load_dotenv

from src.route.pdf_csv_routes import pdf_csv
from src.route.pdf_excel_routes import pdf_excel

load_dotenv()


app = Flask(__name__)
app.config["UPLOAD_FOLDER"] = getenv("UPLOAD_FOLDER")


app.register_blueprint(pdf_csv, pdf_excel)
