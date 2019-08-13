import pandas as pd
import numpy as np
from math import isnan 

dtypes = {
    "csv":pd.read_csv,
    "json":pd.read_json
}

class Brief():
    def __init__(self, file, dtype, *args, **kwargs):
        self.frame = dtypes[dtype](file)
        self.colums = self.frame.columns
        self.catcols = self.frame._get_numeric_data().columns
        self.numcols = [col for col in self.colums if col not in self.catcols]
        self.colum_type = {}
        for i in self.catcols:
            self.colum_type.update({
                i:"cat"
            })
        for i in self.numcols:
            self.colum_type.update({
                i: "num"
            })


    def head(self):
        head = self.frame.head().fillna("nan").T.to_dict()
        return head

    def dtypes(self):
        d = self.frame.dtypes.to_dict()
        ret = []
        for col in d:
            ret.append({"col": col, "dtype": d[col].name})
        return ret                    

    def describe(self):
        a = self.frame.describe().to_dict()
        return [[col, a[col]] for col in a]

    def nunique(self):
        d = self.frame.nunique()
        return [{"col": col, "nuniuqe": int(d[col]),"type":self.colum_type[col]} for col in d.index]

    def nullvals(self):
        d = self.frame.isnull().sum()
        return [{"col": col, "nulls": int(d[col])} for col in d.index]


if __name__ == "__main__":
    df = Brief("../extras/master.csv","csv")

    head = df.head()


    for i in head:
        pass

    print (head)
