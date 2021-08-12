from flask import Flask, abort, jsonify, request
from flask_cors import CORS, cross_origin

# from .run_generation import generate_text
from emotion import analyzeText
app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route("/")
def default():
    return "Under development"

@app.route("/emotion", methods=['POST'])
@cross_origin()
def get_gen():
    data = request.json
    print(request, data)
    if data == None or 'text' not in data or len(data['text']) == 0:
        abort(400)
    else:
        text = data['text']
        result = analyzeText(text)
        return jsonify({'result': result})