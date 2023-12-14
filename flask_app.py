from flask import Flask, request, jsonify
from requests_toolbelt.multipart.encoder import MultipartEncoder
import requests
import json
import fetch_api_key

app = Flask(__name__)

SERVER = "http://127.0.0.1:9999"
APIKEY = fetch_api_key.fetch_api()

@app.route("/")
def home():
    return "Hello, World!"
@app.route("/api/v1/upload",methods=["POST"])
def upload_file():
    if 'file' not in request.files:
        return "No file part", 400

    file = request.files['file']
    if file.filename == '':
        return "No selected file", 400

    multipart_data = MultipartEncoder(fields={'file': (file.filename, file.stream, 'application/octet-stream')})
    headers = {'Content-Type': multipart_data.content_type, 'Authorization': APIKEY}
    response = requests.post(SERVER + '/api/v1/upload', data=multipart_data, headers=headers)
    
    print("respojse from mobsf is ",response.text)
    return response.text, response.status_code
    

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)