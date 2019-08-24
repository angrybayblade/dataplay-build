import pandas as pd
import numpy as np
from math import isnan 

dtypes = {
    "csv":pd.read_csv,
    "json":pd.read_json
}

class DataFrame:
    def __init__(self, file, dtype, *args, **kwargs):
        self.frame = pd.read_csv(file)

    def head(self):
        return self.frame.head().values.tolist()

    def describe(self):
        a = self.frame.describe().T
        return [{"name":x,"data":y} for x,y in zip(a.index,a.values.astype(int).tolist())]

    def columns(self):
        a = self.frame.nunique()
        b = self.frame.dtypes.apply(lambda x:str(x))
        c = self.frame.isnull().sum()
        getType = lambda x: "cat" if x <= 10 else "num"
        return [
            {
                "name":a,
                "type":getType(b),
                "nunique":b,
                "dtype":c,
                "nullvals":d
            } for a,b,c,d in zip(
                a.index,
                a.values.astype(float),
                b.values,
                c.values.astype(float)
            )
        ]

    def getColumn(self,col):
        return self.frame[col].head().values.tolist()

if __name__ == "__main__":
    df = DataFrame("../../extras/housing.csv","csv")
    print (df.columns())