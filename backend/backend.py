from flask import Flask, jsonify, Response

from main import create_ean8_code, \
    create_ean13_code, create_ean13_image_xml, create_ean8_image_xml

app = Flask(__name__)


@app.route("/barcodes")
def list_barcodes():
    return jsonify(["ean8", "ean13"])


@app.route("/barcode8/<string:barcode>")
def barcode8(barcode):
    return Response(create_ean8_code(barcode), mimetype="text/plain")


@app.route("/barcode13/<string:barcode>")
def barcode13(barcode):
    return Response(create_ean13_code(barcode), mimetype="text/plain")


@app.route("/bc8_svg/<barcode>")
def generate_bc8_svg(barcode):
    return Response(create_ean8_image_xml(barcode), mimetype="image/svg+xml")


@app.route("/bc13_svg/<barcode>")
def generate_bc13_svg(barcode):
    return Response(create_ean13_image_xml(barcode), mimetype="image/svg+xml")
