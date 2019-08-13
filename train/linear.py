from sklearn.linear_model import LinearRegression

class Linear:
    def __init__(self,train_features,training_labels,testing_features,testing_labels,hyperparams=None):
        self.model = LinearRegression(**hyperparams)
        #self.model.fit(train_features, training_labels)
        print (self.model)
        
    def predict(self,features):
        return self.model.predict(features)

    def perform_cross_valid(self):
        return matrix
