from flask import Flask, jsonify, Response
from flask import request

from main import create_ean8_code, create_ean13_code, create_ean13_image_xml, create_ean8_image_xml

app = Flask(__name__)


@app.route("/barcodes")
def list_barcodes():
    return jsonify(["ean8", "ean13"])


@app.route("/barcode/<barcode_type>/<data>")
def barcode(barcode_type: str, data: str):
    if (barcode_type := barcode_type.lower()) not in {'ean8', 'ean13'}:
        return Response(f'Unknown barcode type: {barcode_type}', status=404)

    accept_header = request.headers.get('Accept')
    if accept_header == 'image/svg+xml':
        return Response(
            {'ean8': create_ean8_image_xml, 'ean13': create_ean13_image_xml}[barcode_type](data),
            mimetype="image/svg+xml"
        )
    elif accept_header == 'text/plain':
        return Response(
            {'ean8': create_ean8_code, 'ean13': create_ean13_code}[barcode_type](data),
            mimetype="text/plain"
        )
