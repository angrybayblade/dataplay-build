from sklearn.linear_model import LinearRegression
from validation import rmse


class Linear:
    def __init__(self,train_features,training_labels,testing_features,testing_labels,hyperparams=None,validation_matric=None):
        self.model = LinearRegression(**hyperparams)
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
