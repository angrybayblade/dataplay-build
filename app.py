from flask import Flask,request,session,jsonify
from flask_cors import CORS
from time import ctime,time
from hashlib import md5
import os
import json
import sys

from preproc.df import DataFrame
from preproc.transform import transform,split
from train.linear import Linear
from train.validation import *
from visualize.plot import *

app = Flask(__name__)
CORS(app)
getHex = lambda x: md5(x.encode()).hexdigest()
app.secret_key = getHex("viraj")

algos = {
    "ml/supervised/regression":Linear
}

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
            print (res.columns)
            return jsonify({
                "cols":res.columns.tolist()
            })

        if data['method'] == 'impute':
            # col = sessions[data['user']]['df'].getColumn(data['column'])
            res = transform(
                            sessions[data['user']]['df'].frame,
                            data['method'],
                    )
            sessions[data['user']]['df'].frame = res['df']
            return jsonify({
                "column":[],#col,
                "trans":[],
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

@app.route("/train",methods=['POST'])
def train():
    data = request.get_json()
    df = sessions[data['user']]['df']

    info = data['model']
    model = algos[info['type']]

    X,x,Y,y = split(
            df.frame[data['features']],
            df.frame[data['label']]
        )

    model = model(
            train_features=X,
            training_labels=Y,
            testing_features=x,
            testing_labels=y,
            hyperparams=info['hyperparams'],
        )
    
    return jsonify({
        "user":"viraj"
    })

@app.route("/visualize",methods=['POST'])
def visulize():
    data = request.get_json()
    print(data)
    x,y,hue = data['x'],data['y'],data['hue']
    x = sessions[data['user']]['df'].frame[x].values
    if y:
        y = sessions[data['user']]['df'].frame[y].values
    if hue:
        hue = sessions[data['user']]['df'].frame[hue].values

    plotData = plot(x=x,y=y,chart=data['chart'],hue=hue)
    return jsonify({
        "chart":plotData
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0",port=8080,threaded=True)
