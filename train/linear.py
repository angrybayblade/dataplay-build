from sklearn.linear_model import LinearRegression

class Linear:
    def __init__(
            self,
            train_features=[[1],[2],[3],[4],[5],[6]],
            training_labels=[1,4,9,16,25,36],
            testing_features=[[7],[8],[9],[10],[11],[12]],
            testing_labels=[49,64,81,100,121,144],
            hyperparams={"n_jobs":50},
            ):
    
        self.model = LinearRegression(**hyperparams)
        self.model.fit(train_features, training_labels)
        # self.validation_metric = validation_metric
        self.testing_features = testing_features
        self.testing_labels = testing_labels
        self.training_features = training_features
        self.testing_labels = training_labels
        self.hyperparams = hyperparams
        
    def predict(self,features):
        return self.model.predict(features)

    def validate(self,validation_metric):
        training_score = validation_metric(
                                self.training_labels,
                                self.model.predict(self.training_features)
                            )
        testing_score = validation_metric(
                                self.testing_labels,
                                self.model.predict(self.testing_features)
                            )

        testing_score = []
        return {
            "training_score":training_score,
            "testing_score":testing_score
        }

if __name__ == "__main__":
    lin=Linear()
    lin.validate()