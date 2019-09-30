from flask import Flask,request,session,jsonify,render_template,send_from_directory,Response
from flask_cors import CORS
from time import ctime,time
from hashlib import md5
import os
import json
import sys

from preproc.df import DataFrame
from preproc.transform import transform,split
from train.linear import Regression as LR
from train.validation import *
from visualize.plot import *

print (os.getcwd())

app = Flask(__name__)
CORS(app)
getHex = lambda x: md5(x.encode()).hexdigest()
app.secret_key = getHex("viraj")

algos = {
    "ml":{
        "supervised":{
            "regression":{
                "linear":LR
            }
        }
    }
}

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


@app.route('/static/css/<path>',methods=['GET'])
def static_css(path):
    file = open("./templates/static/css/{}".format(path),"r").read()
    return  Response(file, mimetype='text/css')

@app.route('/static/js/<path>',methods=['GET'])
def static_js(path):
    if ".map" in path:
        return  Response("", mimetype='text/javascript')    
    file = open("./templates/static/js/{}".format(path),"r").read()
    return  Response(file, mimetype='text/javascript')

@app.route("/",methods=['GET'])
def index():
    return render_template("index.html")

    
@app.route("/<path>",methods=['GET'])
def index_path(path):
    print (path)
    return render_template("index.html")


@app.route("/upload",methods=['POST'])
def upload():
    data = request.form
    request.files['data'].save(
        os.path.join(
                os.getcwd(),"data","{}.csv".format(data['user']),
            )
        )

    df = DataFrame(os.path.join(
                os.getcwd(),"data","{}.csv".format(data['user']),
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

@app.route("/overview",methods=['POST'])
def overview():
    data = request.get_json()
    df = sessions[data['user']]['df']
    # print (type(df))
    return jsonify({
            "head":df.head(),
            "description":df.describe(),
            "columns":df.columns(),
            "file_name":data['filename']
        })

# Transform.py

@app.route("/transform",methods=['POST'])
def getcolumns():
    data = request.get_json()
    if "method" in data:
        if data['method'] == 'Select':
            return jsonify(
                dict(
                    column=sessions[data['user']]['df'].getColumn(data['column']),
                    trans=[]
                )
            )
        if data['save']:
            res = transform(
                        data['column'],
                        data['method'],
                        save=True,
                        df=sessions[data['user']]['df']
                )
            sessions[data['user']]['df'].frame = res
            print (res.columns)
            return jsonify(
                    dict(
                        cols= res.columns.tolist(),
                        status=True
                    )
                )

        col = sessions[data['user']]['df'].getColumn(data['column'])
        return jsonify({
            "column":col,
            "trans":transform(
                        sessions[data['user']]['df'].frame[[data['column']]],
                        data['method'],
                ),
            })
    else:
        if data['column'] == "Select":
            return jsonify(
                    dict(
                        column=[]
                    )
                )
        col = sessions[data['user']]['df'].getColumn(data['column'])
        return jsonify({
            "column":col
        })

@app.route("/train",methods=['POST'])
def train():
    data = request.get_json()
    path = data['traindata']['type'].split("/")
    model = algos[path[0]][path[1]][path[2]][path[3]]
    df = sessions[data['user']]['df'].frame
    X,x,Y,y = split(df,data['label'],data['features'])

    model = model(X,x,Y,y,data['traindata']['hyperparams'])
    model.fit()
    return jsonify(model.validate())

@app.route("/visualize",methods=['POST'])
def visulize():
    data = request.get_json()
    return jsonify(plot(sessions[data['user']]['df'].frame,**data))

if __name__ == "__main__":
    app.run(host="0.0.0.0",port=8080,threaded=True)
