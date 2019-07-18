"""
Process data
"""

import pandas as pd
import yaml

config = yaml.safe_load(open("process_data.yml"))

# Read input data
a_df = pd.read_csv(**config["input"]["a"])
b_df = pd.read_excel(**config["input"]["b"])

# Data exploration
print(a_df.shape)
print(b_df.shape)

print(a_df.head())
print(b_df.head())

print(a_df.info())
print(b_df.info())

# Data processing
# ...

# Export results
a_df.to_csv(**config["output"]["a"])
b_df.to_csv(**config["output"]["b"])