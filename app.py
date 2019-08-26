from flask import Flask,request,session,jsonify
from flask_cors import CORS
from time import ctime,time
from hashlib import md5
import os
import json
import sys

from preproc.df import DataFrame
from preproc.transform import transform

app = Flask(__name__)
CORS(app)
getHex = lambda x: md5(x.encode()).hexdigest()
app.secret_key = getHex("viraj")

@app.route("/",methods=['GET'])
def index():
    return jsonify({
        "msg":"hello"
    })

dfTemplate = {
    "df":None,
    "trnasform":[],
    "visualize":{},
    "train":{},
    "user":{}
}

sessions = {

}

def createSession(**kwargs):
    kwargs.update({
        "trnasform":[],
        "visualize":{},
        "train":{},
    })
    sessions.update({kwargs['user']:kwargs})
    return kwargs


df = DataFrame(os.path.join(
                "C:\\workspace\\mlplay\server\\data","viraj.csv"
            ),"csv")

session = createSession(
                user="viraj",
                df=df
            )

@app.route("/upload",methods=['GET','POST'])
def upload():
    data = request.form
    request.files['data'].save(
        os.path.join(
                "C:\\workspace\\mlplay\server\\data",f"{data['user']}.csv"
            )
        )

    df = DataFrame(os.path.join(
                "C:\\workspace\\mlplay\server\\data",f"{data['user']}.csv"
            ),"csv")

    session = createSession(
                user=data['user'],
                df=df
            )

    return jsonify({
            "head":df.head(),
            "description":df.describe(),
            "columns":df.columns(),
            "file_name":request.files['data'].filename
        })

# Transform.py

@app.route("/transform",methods=['POST'])
def getcolumns():
    data = request.get_json()
    if "method" in data:
        if data['save']:
            res = transform(
                        data['column'],
                        data['method'],
                        save=True,
                        df=sessions[data['user']]['df']
                )
            sessions[data['user']]['df'].frame = res
            return jsonify({
                "cols":res.columns.tolist()
            })

        col = sessions[data['user']]['df'].getColumn(data['column'])
        return jsonify({
            "column":col,
            "trans":transform(
                        sessions[data['user']]['df'].frame[[data['column']]],
                        data['method'],
                ),
            })
    else:
        col = sessions[data['user']]['df'].getColumn(data['column'])
        return jsonify({
            "column":col
        })

if __name__ == "__main__":
    app.run(host="0.0.0.0",port=8080,threaded=True)
