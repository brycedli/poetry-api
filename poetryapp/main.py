from flask import Flask, abort, jsonify, request
from flask_cors import CORS, cross_origin
from textgenrnn import textgenrnn

# from .run_generation import generate_text
from emotion import analyzeText
app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
textgen = textgenrnn(weights_path='weights/colaboratory_weights.hdf5',
                       vocab_path='weights/colaboratory_vocab.json',
                       config_path='weights/colaboratory_config.json')

@app.route("/")
def default():
    return "Under development"

@app.route("/generate", methods=['POST'])
@cross_origin()
def get_gen():
    data = request.json
    if data == None or 'text' not in data or len(data['text']) == 0:
        abort(400)
    else:
        prefixText = data['text']
        result = textgen.generate(return_as_list=True,prefix=prefixText, temperature=1.0, max_gen_length=50)
        return jsonify({'result': result})


@app.route("/emotion", methods=['POST'])
@cross_origin()
def get_emotion():
    data = request.json
    if data == None or 'text' not in data or len(data['text']) == 0:
        abort(400)
    else:
        text = data['text']
        result = analyzeText(text)
        return jsonify({'result': result})