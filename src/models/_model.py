import pandas as pd
from ._log_reg import LogReg
from ._naive_bayes import NVB

class PredictionModel():
    def __init__(df: pd.DataFrame, model_name: str):

        if df == None:
            raise FileNotFoundError("The DataFrame is empty")
        
        X = df.iloc[:, :-1]
        y = df.iloc[:, -1:]

        if model_name == "LogReg":
            return LogReg(X, y)
        
        if model_name == "NVB":
            return NVB(X, y)
        
        else:
            raise ModuleNotFoundError("No such model exists")