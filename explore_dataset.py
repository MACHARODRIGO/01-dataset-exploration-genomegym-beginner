import pandas as pd

df = pd.read_csv('data/dna_sequences.csv')
print(df)

print("\nDataFrame Info:")
print(df.info())

print("\nSummary Statistics:")
print(df.describe())