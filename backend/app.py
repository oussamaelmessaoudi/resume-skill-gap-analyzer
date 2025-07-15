from flask import Flask, jsonify, request
from flask_cors import CORS,cross_origin

app = Flask(__name__)
CORS(app)

@app.route('/analyze',methods=['POST'])
def analyze():
    data = request.json

def extract_resume_skills(file):
    
def extract_jd_skills(file):


if __name__ == "__main__":
    app.run(debug=True)