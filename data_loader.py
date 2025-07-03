import pandas as pd

class DataLoader:
    def __init__(self, url=None):
        self.url = url or "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/tips.csv"

    def load_data(self):
        df = pd.read_csv(self.url)
        return df