from flask import Flask, jsonify, Response

from main import create_ean8_code, \
    create_ean13_code, create_ean13_image_xml, create_ean8_image_xml

app = Flask(__name__)


@app.route("/barcodes")
def list_barcodes():
    return jsonify(["ean8", "ean13"])


from flask import request


@app.route("/barcode8/<barcode>")
def barcode8(barcode):
    accept_header = request.headers.get('Accept')
    if accept_header == 'image/svg+xml':
        return Response(create_ean8_image_xml(barcode), mimetype="image/svg+xml")
    elif accept_header == 'text/plain':
        return Response(create_ean8_code(barcode), mimetype="text/plain")


@app.route("/barcode13/<barcode>")
def barcode13(barcode):
    accept_header = request.headers.get('Accept')
    if accept_header == 'image/svg+xml':
        return Response(create_ean13_image_xml(barcode), mimetype="image/svg+xml")
    elif accept_header == 'text/plain':
        return Response(create_ean13_code(barcode), mimetype="text/plain")
