from flask import Flask, request, jsonify
import json
import requests

app = Flask(__name__)


@app.route("/callback", methods=["POST"])
def callback():
    data = request.json
    # print(f"Received data: {data}")
    print(data)
    return jsonify({"message": "Data received successfully!"})


@app.route("/")
def get_client_ip():
    response = requests.get('http://api.ipify.org')
    print(response.text)
    return response.text


if __name__ == "__main__":
    app.run("0.0.0.0", 7575)
