import os 
import sys 
import numpy as np
import pandas as  pd
import dill
from src.execption import CustomException
from sklearn.metrics import r2_score
from sklearn.model_selection import GridSearchCV
def save_object(file_path,obj):
    try:
        dir_path=os.path.dirname(file_path)
        os.makedirs(dir_path,exist_ok=True)
        with open(file_path,'wb') as file_obj:
            dill.dump(obj,file_obj)

    except Exception as e:
        raise CustomException(e,sys)
    


def evaluate_model(X_train,Y_train,X_test,Y_test,models,params):

    try:
        report={}
        for i in range(len(list(models))):
            model=list(models.values())[i]

            para=params[list(models.keys())[i]]
            
            gs=GridSearchCV(model,para,cv=3)
            gs.fit(X_train,Y_train)
            
            model.set_params(**gs.best_params_)
            model.fit(X_train,Y_train)
            #model.fit(X_train,Y_train)

            Y_train_pred=model.predict(X_train)
            Y_test_pred=model.predict(X_test)

            train_model_score=r2_score(Y_train,Y_train_pred)
            test_model_Score=r2_score(Y_test,Y_test_pred)

            report[list(models.keys())[i]]=test_model_Score

            return report
    except Exception as e:
        raise CustomException(e,sys)
    

def load_objects(file_path):
    try:
        with open(file_path,'rb') as file_obj:
            return dill.load(file_obj)
    except Exception as e:
        raise CustomException(e,sys)    