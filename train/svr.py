from sklearn.svm import SVR
from validation import *


class Linear:
    def __init__(self,train_features,training_labels,testing_features,testing_labels,hyperparams=None,validation_metric=None):
        self.model = sv(**hyperparams)
        #self.model.fit(train_features, training_labels)
        self.validation_metric = validation_metric
        self.hyperparams = hyperparams
        
    def predict(self,features):
        return self.model.predict(features)

    def perform_cross_valid(self):
        return matrix

    def validate(self):
        if self.validation_matric:
            if self.validation_metric == "rmse":
                #perfrom rmse
                return rmse()
        else:
            #perform rmse
            return {
                
            }
