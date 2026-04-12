import pandas as pd

csv_file = "PlayerStatistics.csv"
parquet_file = "PlayerStatistics.parquet"

df = pd.read_csv(csv_file)
df.to_parquet(parquet_file, engine="pyarrow")

print(f"Converted {csv_file} -> {parquet_file}")
