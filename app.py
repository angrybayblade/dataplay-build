from flask import Flask,request,session,jsonify
from flask_cors import CORS
from time import ctime,time
from hashlib import md5
import os
import json
import sys

from preproc import brief
from train import linear

models = {
    "linear":linear.Linear,
}

app = Flask(__name__)
CORS(app)
getHex = lambda x: md5(x.encode()).hexdigest()
app.secret_key = getHex("viraj")

@app.route("/",methods=['GET'])
def index():
    return jsonify({
        "msg":"hello"
    })

dataFrames ={

}

@app.route("/upload",methods=['GET','POST'])
def upload():
    data = request.form
    request.files['data'].save(
        os.path.join(
                "C:\\workspace\\mlplay\server\\data",f"{data['user']}.csv"
            )
        )
    df = brief.Brief(
        os.path.join("C:\\workspace\\mlplay\server\\data", f"{data['user']}.csv"),
        "csv"
    )

    dataFrames[data['user']] = df

    return jsonify({
        "head":list(df.head().values()),
        "columns":list(df.frame.columns),
        "dtypes":df.dtypes(),
        "nuniques":df.nunique(),
        "nullvals":df.nullvals(),
        "description":df.describe()
        })


if __name__ == "__main__":
    app.run(host="0.0.0.0",port=8080,threaded=True)
