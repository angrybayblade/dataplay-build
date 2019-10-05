from . import validation

class Train:
    def __init__(self, *args, **kwargs):
        self.X = kwargs['X']
        self.x = kwargs['x']
        self.Y = kwargs['Y']
        self.y = kwargs['y']
        self.type = kwargs['type']
        exec("from {} import {}".format(kwargs['package'],kwargs['name']))
        exec("self.model = {}".format(kwargs['name']))
        self.model = self.model(**kwargs['hyperparams'])

    def fit(self):
        try:
            self.model.fit(self.X,self.Y)
            return True,None
        except ValueError as e:
            return False,e
        
    def validate(self):
        return validation.validate(
                    self.type,
                    self.model,
                    self.X,
                    self.x,
                    self.Y,
                    self.y,
                )