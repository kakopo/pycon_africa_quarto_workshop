import pandas as pd
import os

data = pd.read_csv("/Users/kopo/Documents/pycon_africa/states.csv")
for _, row in data.iterrows():
    os.system(f'quarto render population_stats.qmd -P state:"{row.state}" --output {row.filename}')