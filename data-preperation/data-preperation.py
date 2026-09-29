from pathlib import Path

import pandas as pd


path = Path("..") / "data" / "Training-data.csv"

if not path.exists(): raise FileNotFoundError
training_data = pd.read_csv(path)

print(training_data.head())

missing_list = training_data.isnull().values.any()
print(missing_list)

