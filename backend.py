from flask import Flask, jsonify, Response
from main import generate_ean8_code, generate_ean13_code, create_ean8_image, create_ean13_image

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/barcodes")
def list_barcodes():
    return jsonify(["ean8", "ean13"])


@app.route("/barcode8/<string:barcode>")
def barcode8(barcode):
    return generate_ean8_code(barcode)


@app.route("/barcode13/<string:barcode>")
def barcode13(barcode):
    return generate_ean13_code(barcode)


@app.route("/bc8_svg/<barcode>")
def generate_bc8_svg(barcode):
    return Response(create_ean8_image(barcode), mimetype="image/svg+xml")


@app.route("/bc13_svg/<barcode>")
def generate_bc13_svg(barcode):
    return Response(create_ean13_image(barcode), mimetype="image/svg+xml")
