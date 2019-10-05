from sklearn.metrics import mean_squared_error,precision_score,recall_score,f1_score,confusion_matrix
import numpy as np

def validate(t,model,X,x,Y,y):
    if t == 'regression':
        train_error = np.sqrt(
                mean_squared_error(
                    Y,model.predict(X)
                )
            )
        test_error = np.sqrt(
                    mean_squared_error(
                    y,model.predict(x)
                )            
            )
        return dict(
                train_error=train_error,
                test_error=test_error,
                type=t
            )

    else:
        y_pred = model.predict(x)
        Y_pred = model.predict(X)
        train_score = f1_score(
                Y,Y_pred
            )
        test_score = f1_score(
                y,y_pred
            )
        confusion_mat = confusion_matrix(y,y_pred).tolist()

        return dict(
                test_score=test_score,
                train_score=train_score,
                confusion=confusion_mat,
                type=t
            )

