from flask import Flask, jsonify
from flask_cors import CORS
import request

app = Flask(__name__)
CORS(app)


if __name__ == "__main__":
    app.run(debug=True)