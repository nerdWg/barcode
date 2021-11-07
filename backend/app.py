from flask import Flask, jsonify, Response
from flask import request

from main import create_code, create_image_xml

app = Flask(__name__)


@app.route("/barcodes")
def list_barcodes():
    return jsonify(["ean8", "ean13", "code39"])


@app.route("/barcode/<barcode_type>", methods=['POST'])
def barcode(barcode_type: str):
    accept_header = request.headers.get('Accept')
    data = request.data.decode('utf-8')
    if accept_header == 'image/svg+xml':
        return Response(create_image_xml(data, barcode_type), mimetype="image/svg+xml")
    elif accept_header == 'text/plain':
        return Response(create_code(data, barcode_type), mimetype="text/plain")
