from sklearn.metrics import mean_squared_error,precision_score,recall_score,f1_score,confusion_matrix,r2_score
import numpy as np
from sklearn.model_selection import cross_val_score

def validate(t,model,X,x,Y,y,cv=100):
    if t == 'regression':
        mse = np.sqrt(
                cross_val_score(
                    model,X,Y,
                    cv=cv,
                    scoring=lambda *args:mean_squared_error(
                        args[2],
                        args[0].predict(
                            args[1]
                        )
                    )
                )
        ).tolist()

        r2_error = cross_val_score(
                    model,X,Y,
                    cv=cv,
                    scoring=lambda *args:r2_score(
                        args[2],
                        args[0].predict(
                            args[1]
                        )
                    )
                ).tolist()


        return dict(
                mse=mse,
                r2_error=r2_error,
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

