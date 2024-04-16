# -*- coding:utf-8 -*-

from crypt import methods
from flask import Flask, jsonify, request
from korquad_predict import *
from bert import QA
import urllib.parse
import time

HOST = "112.160.206.172"

app = Flask(__name__)


@app.route('/', methods=['GET'])

def index():
    
    uid = request.args.get("uid")
    q = urllib.parse.unquote(request.args.get("q"))

    ans = make_prediction(uid, q, model)
    # ans = uid
    return ans


if __name__ == "__main__":
    model = QA('./output')
    app.run(host=HOST, debug=True)
