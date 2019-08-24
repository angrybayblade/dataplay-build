from sklearn.svm import SVR
from validation import *

evals={
"root_mean_squared_error":rmse,"mean_squared_error":mse,"mean_absolute_error":mae,"r2_score":r2,"mean_squared_log_error":log,"explained_variance_score":var_score,"max_error":max
}
class Support_Regressor:
    def __init__(self,train_features=[[1],[2],[3],[4],[5],[6]],training_labels=[1,4,9,16,25,36],testing_features=[[7],[8],[9],[10],[11],[12]],testing_labels=[49,64,81,100,121,144],hyperparams=None,validation_metric="root_mean_squared_error"):
        self.model = SVR(**hyperparams)
        self.model.fit(train_features, training_labels)
        self.validation_metric = validation_metric
        self.hyperparams = hyperparams
        self.train_features=train_features
        self.training_labels=training_labels
        self.testing_features=testing_features
        self.testing_labels=testing_labels
        
    def predict(self,features):
        return self.model.predict(features)

    def perform_cross_valid(self):
        return matrix

    def validate(self):
         print (evals[self.validation_metric](self.testing_labels,self.predict(self.testing_features)))
sv=Support_Regressor()
sv.validate()