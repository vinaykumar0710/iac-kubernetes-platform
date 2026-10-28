import os
from flask import Flask, jsonify

app = Flask(__name__)
APP_VERSION = os.getenv("APP_VERSION", "1.0.0")


@app.get("/")
def home():
    return jsonify(
        application="iac-platform-app",
        version=APP_VERSION,
        status="running",
    )


@app.get("/healthz")
def health():
    return jsonify(status="healthy"), 200


@app.get("/readyz")
def ready():
    return jsonify(status="ready"), 200
