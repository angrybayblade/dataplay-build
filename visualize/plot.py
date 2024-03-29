import numpy as np

layoutTamp = {
                "width": "110%", 
                "height": "110%", 
                "title": {
                    "text":'Plot Title',
                    "font": {
                    "family": 'Courier New, monospace',
                    "size": 24
                    },
                    "xref": 'paper',
                },
                "xaxis": {
                    "title": {
                    "text": 'X',
                    "font": {
                        "family": 'Courier New, monospace',
                        "size": 18,
                        "color": '#7f7f7f'
                    }
                    },
                },
                "yaxis": {
                    "title": {
                    "text": 'Y',
                    "font": {
                        "family": 'Courier New, monospace',
                        "size": 18,
                        "color": '#7f7f7f'
                    }
                }
            }
        }

def getTraceName(x):
    if type(x) == np.int64:
        return int(x)

    elif type(x) == str:
        return x

    elif np.isnan(x):
        return str('NaN')

    return x

def plot(df,x,y,hue,chart,user=None):
    if chart['type'] == "bar":
        if y != "Select" and y:
            if hue and hue != "Select":
                print (hue)
                tdf = df[[x,y]].groupby(x).sum()[y]
                chart['x'] = tdf.index.tolist()
                chart['y'] = tdf.values.tolist()
                traces = [chart]
                layout = layoutTamp.copy()
                layout['title']['text'] = x.replace("_"," ").title()
                layout['xaxis']['title']['text'] = x.replace("_"," ").title()
                layout['yaxis']['title']['text'] = "Average " + y.replace("_"," ").title()
                return {
                        "data":traces,
                        "layout":layout
                        }    

            tdf = df[[x,y]].groupby(x).mean()[y]
            chart['x'] = tdf.index.tolist()
            chart['y'] = tdf.fillna(method='ffill').values.tolist()
            traces = [chart]
            layout = layoutTamp.copy()
            layout['title']['text'] = x.replace("_"," ").title()
            layout['xaxis']['title']['text'] = x.replace("_"," ").title()
            layout['yaxis']['title']['text'] = "Average " + y.replace("_"," ").title()
            return {
                    "data":traces,
                    "layout":layout
                    }

        else:
            if hue and hue != "Select":
                traces = []    
                tdf = df[[x,hue]]

                for i in tdf[hue].unique():
                    trace = chart.copy()
                    values = tdf[tdf[hue] == i][x].value_counts()
                    trace.update({'x' : values.index.tolist() })
                    trace.update({'y' : values.values.tolist() })
                    
                    trace.update({'name': getTraceName(i) })    
                    traces.append(trace)


                layout = layoutTamp.copy()
                layout['title']['text'] = x.replace("_"," ").title()
                layout['xaxis']['title']['text'] = x.replace("_"," ").title()
                layout['yaxis']['title']['text'] = None
                return {
                        "data":traces,
                        "layout":layout
                        }

            tdf = df[x].value_counts()
            chart['x'] = tdf.index.tolist()
            chart['y'] = tdf.values.tolist()
            traces = [chart]
            layout = layoutTamp.copy()
            layout['title']['text'] = x.replace("_"," ").title()
            layout['xaxis']['title']['text'] = x.replace("_"," ").title()
            layout['yaxis']['title']['text'] = None
            return {
                    "data":traces,
                    "layout":layout
                    }

    elif chart['type'] == "line":
        print (chart['type'])
        if y != "Select" and y:
            tdf = df[[x,y]].groupby(x).sum()[y]
            chart['x'] = tdf.index.tolist()
            chart['y'] = tdf.values.tolist()
            traces = [chart]
            layout = layoutTamp.copy()
            layout['title']['text'] = x.replace("_"," ").title()
            layout['xaxis']['title']['text'] = x.replace("_"," ").title()
            layout['yaxis']['title']['text'] = y.replace("_"," ").title() + " Total"
            return {
                    "data":traces,
                    "layout":layout
                    }

        else:
            tdf = df[x].value_counts()
            chart['x'] = tdf.index.tolist()
            chart['y'] = tdf.values.tolist()
            traces = [chart]
            layout = layoutTamp.copy()
            layout['title']['text'] = x.replace("_"," ").title()
            layout['xaxis']['title']['text'] = x.replace("_"," ").title()
            layout['yaxis']['title']['text'] = None
            return {
                    "data":traces,
                    "layout":layout
                    }

    elif chart['type'] == 'scatter':
        if hue and hue != "Select":
            
            traces = []    
            tdf = df[[x,y,hue]]


            for i in tdf[hue].unique():
                trace = chart.copy()
                trace.update({'x' : tdf[tdf[hue] == i][x].fillna(method='ffill').astype(int).values.tolist()})
                trace.update({'y' : tdf[tdf[hue] == i][y].fillna(method='ffill').astype(int).values.tolist()})
                trace.update({'name':i})
                traces.append(trace)

            layout = layoutTamp.copy()
            layout['title']['text'] = x.replace("_"," ").title() +" vs "+ y.replace("_"," ").title()
            layout['xaxis']['title']['text'] = x.replace("_"," ").title()
            layout['yaxis']['title']['text'] = y.replace("_"," ").title()
            return {
                    "data":traces,
                    "layout":layout
                    }
        
        else:
            chart['x'] = df[x].fillna(method='ffill').values.tolist()
            chart['y'] = df[y].fillna(method='ffill').values.tolist()
            traces = [chart]
            layout = layoutTamp.copy()
            layout['title']['text'] = x.replace("_"," ").title() +" vs "+ y.replace("_"," ").title()
            layout['xaxis']['title']['text'] = x.replace("_"," ").title()
            layout['yaxis']['title']['text'] = y.replace("_"," ").title()
            return {
                    "data":traces,
                    "layout":layout
                    }

    elif chart['type'] == 'histogram':
        chart['x'] = df[x].fillna(method='ffill').values.tolist()
        traces = [chart]
        layout = layoutTamp.copy()
        layout['title']['text'] = x.replace("_"," ").title() 
        layout['xaxis']['title']['text'] = x.replace("_"," ").title()
        layout['yaxis']['title']['text'] = ""
        return {
                "data":traces,
                "layout":layout
                }

    elif chart['type'] == 'pie':
        tdf = df[x].value_counts()
        chart['values'] = tdf.values.tolist()
        chart['labels'] = tdf.index.tolist()
        traces = [chart]
        layout = layoutTamp.copy()
        layout['title']['text'] = x.replace("_"," ").title()
        del layout['xaxis'],layout['yaxis']
        return {
                "data":traces,
                "layout":layout
                }

    elif chart['type'] == 'donut':
        tdf = df[x].value_counts()
        chart['values'] = tdf.values.tolist()
        chart['labels'] = tdf.index.tolist()
        chart.update({'name':x.replace("_"," ").title()})
        traces = [chart]
        layout = layoutTamp.copy()
        layout['title']['text'] = x.replace("_"," ").title()
        del layout['xaxis'],layout['yaxis']
        return {
                "data":traces,
                "layout":layout
                }

    elif chart['type'] == 'box':
        if y != "Select" and y:
            traces = []
            tdf = df[[x,y]]

            for i in tdf[y].unique():
                trace = chart.copy()
                trace.update({'y' : tdf[tdf[y] == i][x].fillna(method="ffill").values.tolist()})
                trace.update({'name':i})
                traces.append(trace)

            layout = layoutTamp.copy()
            layout['title']['text'] = x.replace("_"," ").title()
            layout['xaxis']['title']['text'] = x.replace("_"," ").title()
            # layout['yaxis']['title']['text'] = y.replace("_"," ").title()
            return {
                    "data":traces,
                    "layout":layout
                    }

        else:
            chart['y'] = df[x].fillna(method="ffill").values.tolist()
            chart.update({'name':x.replace("_"," ").title()})
            traces = [chart]
            layout = layoutTamp.copy()
            layout['title']['text'] = x.replace("_"," ").title()
            del layout['xaxis'],layout['yaxis']
            return {
                    "data":traces,
                    "layout":layout
                    }
        


