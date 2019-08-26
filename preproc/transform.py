from sklearn.impute import SimpleImputer
from sklearn.preprocessing import MinMaxScaler,LabelEncoder,StandardScaler,Normalizer
from pandas import get_dummies,read_csv


def impute(x,save=False):
    imp = SimpleImputer(strategy="median")
    return [float(x[0]) for x in imp.fit_transform(x)[:5]]

def labelenc(x,save=False):
    imp = LabelEncoder()
    return imp.fit_transform(x).tolist()[:5]

def dummies(x,save=False):
    if not save:
        imp = get_dummies(x[x.columns[0]]).head()
        return {
                "columns":imp.columns.tolist(),
                "values":imp.values.tolist()
            }
    else:
        cols = get_dummies(x)
        return cols       

def minmax(x,save=False):
    imp = MinMaxScaler(feature_range=(1,10))
    return [float(x[0]) for x in imp.fit_transform(x)[:5]]

def stdscale(x,save=False):
    imp = StandardScaler()
    return [float(x[0]) for x in imp.fit_transform(x)[:5]]

def normalize(x,save=False):
    imp = Normalizer()
    return [float(x[0]) for x in imp.fit_transform(x)[:5]]

t = {
        "labelenc":labelenc,
        "dummy":dummies,
        "minmax":minmax,
        "standardscaler":stdscale,
        "normalize":normalize
}


def transform(col,trans,save=False,df=None):
    if save:
        cols = dummies(
             df.frame[col],
             save=True
        )
        return df.frame.join(cols).drop(columns=[col])

    return t[trans](col,save=save)


if __name__ == "__main__":
        df = read_csv("../../extras/housing.csv")
        print (dummies(df['ocean_proximity']))