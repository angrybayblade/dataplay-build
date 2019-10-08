from sklearn.metrics import mean_squared_error,precision_score,recall_score,f1_score,confusion_matrix
import numpy as np
from sklearn.model_selection import cross_val_score

def validate(t,model,X,x,Y,y,cv=100):
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
        reg_lin = model.predict(X)
        return dict(
                train_error=train_error,
                test_error=test_error,
                reg_line = dict(
                    scatter=[X,Y],
                    reg_line=[reg_lin,Y]
                ),
                type=t
            )

    else:
        f1_cv = cross_val_score(
                model,X,Y,
                cv=cv,
                scoring=lambda *args:f1_score(
                    args[2],
                    args[0].predict(
                        args[1]
                    )
                )
            ).tolist()

        pres_cv = cross_val_score(
                model,X,Y,
                cv=cv,
                scoring=lambda *args:precision_score(
                    args[2],
                    args[0].predict(
                        args[1]
                    )
                )
            ).tolist()

        rec_cv = cross_val_score(
                model,X,Y,
                cv=cv,
                scoring=lambda *args:recall_score(
                    args[2],
                    args[0].predict(
                        args[1]
                    )
                )
            ).tolist()
        
        confusion_mat = confusion_matrix(y,model.predict(x)).tolist()

        return dict(
                f1_cv=f1_cv,
                rec_cv=rec_cv,
                pres_cv=pres_cv,
                conf_mat=confusion_mat,
                type=t
            )

