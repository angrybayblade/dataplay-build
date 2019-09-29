from sklearn.linear_model import LinearRegression

class Regression:
    def __init__(X,x,Y,y,params):
        self.X = X
        self.x = x
        self.Y = Y
        self.y = y
        self.params = params

        return self


if __name__ == "__main__":
    lin=Linear()
    lin.validate()