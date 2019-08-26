from sklearn.linear_model import LinearRegression
from validation import *

class Linear:
    def __init__(self,train_features=[[1],[2],[3],[4],[5],[6]],training_labels=[1,4,9,16,25,36],testing_features=[[7],[8],[9],[10],[11],[12]],testing_labels=[49,64,81,100,121,144],hyperparams={"n_jobs":50},validation_metric="root_mean_squared_error"):
        self.model = LinearRegression(**hyperparams)
        self.model.fit(train_features, training_labels)
        self.validation_metric = validation_metric
        self.testing_features=testing_features
        self.testing_labels=testing_labels
        self.hyperparams = hyperparams
        
    def predict(self,features):
        return self.model.predict(features)

    def perform_cross_valid(self):
        return matrix

    def validate(self):
        print (evals[self.validation_metric](self.testing_labels,self.predict(self.testing_features)))
        
lin=Linear()
lin.validate()