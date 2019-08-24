from sklearn.metrics import mean_squared_error,mean_absolute_error,r2_score,mean_squared_log_error
from sklearn.metrics import explained_variance_score,max_error
import numpy as np
def rmse(y_true,y_pred):
    #perfrom rmse
    return(np.sqrt(mean_squared_error(y_true,y_pred)))

def mse(y_true,y_pred):
    return(mean_squared_error(y_true,y_pred))

def mae(y_true,y_pred):
    return(mean_absolute_error(y_true,y_pred))


def r2(y_pred,y_true):
    return(r2_score(y_true,y_pred))

def log(y_true,y_pred):
    return(mean_squared_log_error(y_true,y_pred))

def var_score(y_true,y_pred):
    return(explained_variance_score(y_true,y_pred))

def max(y_true,y_pred):
    return(max_error(y_true,y_pred))

