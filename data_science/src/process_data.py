"""
Process data
"""

import pandas as pd
import yaml

config = yaml.safe_load(open("process_data.yml"))

# Read input data
df = pd.read_csv(**config["input"])

# Data exploration
print(df.shape)

print(df.head())

print(df.info())

# Data processing
df.dropna(inplace=True)

# Export results
df.to_csv(**config["output"])