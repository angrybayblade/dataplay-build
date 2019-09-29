from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

class Regression:
    def __init__(self,X,x,Y,y,params):
        self.X = X
        self.x = x
        self.Y = Y
        self.y = y
        self.params = params
        self.model = LinearRegression(**params)

    def fit(self):
        self.model.fit(self.X,self.Y)
    
    def validate(self):
        return dict(
            train=mean_squared_error(
                self.model.predict(self.X),self.Y
            ),
            test=mean_squared_error(
                self.model.predict(self.x),self.y
            ),
            type="mse"
        )


if __name__ == "__main__":
    lin=Linear()
    lin.validate()