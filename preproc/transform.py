from sklearn.impute import SimpleImputer
from sklearn.preprocessing import MinMaxScaler,LabelEncoder,StandardScaler,Normalizer,Imputer
from pandas import get_dummies,read_csv,DataFrame
from sklearn.model_selection import train_test_split

def impute(x,save=False):
    imp = SimpleImputer(strategy="median")
    if save:
        return imp.fit_transform(x)
    return [float(x[0]) for x in imp.fit_transform(x)[:5]]

def labelenc(x,save=False):
    imp = LabelEncoder()
    if save:
        return imp.fit_transform(x)
    return imp.fit_transform(x).reshape(-1,1).tolist()[:5]

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
    if save:
        return imp.fit_transform(x)

    return [[float(x[0])] for x in imp.fit_transform(x)[:5]]


def stdscale(x,save=False):
    imp = StandardScaler()
    if save:
        return imp.fit_transform(x)
    return [[float(x[0])] for x in imp.fit_transform(x)[:5]]


def normalize(x,save=False):
    imp = Normalizer()
    if save:
        return imp.fit_transform(x)
    return [[float(x[0])] for x in imp.fit_transform(x)[:5]]

t = {
        "Label Encoder":labelenc,
        "One Hot Encode":dummies,
        "MinMax Scaler":minmax,
        "Standard Scaler":stdscale,
        "Normalizer":normalize
}

def split(x,y):
    return train_test_split(x,y)

imp = Imputer(strategy="median")

def transform(col,trans,save=False,df=None):
    if trans != "Imputer":
        if save:
            if trans == "One Hot Encode":
                cols = dummies(
                df.frame[col],
                    save=True
                )
                return df.frame.join(cols).drop(columns=[col])
            else:
                df.frame[col] = t[trans](df.frame[[col]],save=True)
                return df.frame

        return t[trans](col)

    return {
        "df": DataFrame(
                data=imp.fit_transform(col),
                columns=col.columns
            )
    }

if __name__ == "__main__":
        df = read_csv("../../extras/housing.csv")
        # print (df['households'])
        print (minmax(df[['households']],save=True))