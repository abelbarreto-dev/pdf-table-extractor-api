from flask import Flask

from src.route.pdf_csv import pdf_csv
from src.route.pdf_excel import pdf_excel


app = Flask(__name__)


app.register_blueprint(pdf_csv, pdf_excel)
