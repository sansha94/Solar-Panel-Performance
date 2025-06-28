import pandas as pd

def fix_dtypes(
  df: pd.DataFrame,
  columns: list
):
  for column in columns:
    df[column] = df[column].astype(float)

  return df
