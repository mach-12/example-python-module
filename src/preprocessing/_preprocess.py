import pandas as pd
from sklearn.preprocessing import StandardScaler
 
class ProcessDataframe():
    def __init__(df: pd.DataFrame):
        if df == None:
            raise FileNotFoundError("The DataFrame is empty")
        
        std_scaler = StandardScaler()
        
        df_scaled = std_scaler.fit_transform(df.iloc[:, :-1])
        df_scaled = pd.concat((df_scaled, df.iloc[:, -1:]), 1)

        print(df_scaled)
        return df_scaled

