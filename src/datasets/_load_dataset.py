import os
import pandas as pd

class DataLoader():
    datasets = []

    def __init__(self):
        self.datasets = os.listdir('src/datasets/data')

    def load_dataset(self, dataset_name: str):
        data_df = None

        try:
            data_df = pd.read_csv(dataset_name)
        except(FileNotFoundError):
            print(f"Dataset named {data_df} not found")
        
        return data_df
    
    def show_datasets(self):
        print(self.datasets)

        
    


dataset = "data/"