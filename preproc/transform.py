from sklearn.impute import SimpleImputer
from sklearn.preprocessing import MinMaxScaler,LabelBinarizer,StandardScaler,Normalizer
# import pandas as pd
# import numpy as np
# df = pd.DataFrame({"x":[1,2,3,np.nan,5,np.nan,7]})

def impute(x):
    imp = SimpleImputer(strategy="median")
    return [float(x[0]) for x in imp.fit_transform(x)[:5]]

def label_bin(x):
    imp = SimpleImputer(strategy="median")
    return [float(x[0]) for x in imp.fit_transform(x)[:5]]

def ohe(x):
    imp = SimpleImputer(strategy="median")
    return [float(x[0]) for x in imp.fit_transform(x)[:5]]

def minmax(x):
    imp = MinMaxScaler()
    return [float(x[0]) for x in imp.fit_transform(x)[:5]]

def stdscale(x):
    imp = StandardScaler()
    return [float(x[0]) for x in imp.fit_transform(x)[:5]]

def normalize(x):
    imp = Normalizer()
    return [float(x[0]) for x in imp.fit_transform(x)[:5]]

t = {
        "lable-bin":label_bin,
        "onehotencoder":ohe,
        "minmax":minmax,
        "standardscaler":stdscale,
        "normalize":normalize
}

def transform(col,trans):
    return t[trans](col)