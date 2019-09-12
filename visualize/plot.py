import numpy as np

def plot(df,x,y,hue,chart,user=None):

    print (chart)

    data = [
                {
                    "x":np.random.rand(100).tolist(),
                    "y":np.random.rand(100).tolist(),
                    "type": "scatter",
                    "mode":"markers",
                    "marker": {"color": "blue"},
                },
            ]
            
    layout = {

    }
    
    return {
            "data":[
                        {
                            "x":np.random.rand(100).tolist(),
                            "y":np.random.rand(100).tolist(),
                            "type": "scatter",
                            "mode":"markers",
                            "marker": {"color": "blue"},
                        },
                    ]
            }