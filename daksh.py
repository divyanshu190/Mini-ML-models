import pandas as pd
from universal_imputer import universal_imputer

df = pd.read_csv("p2_data.csv")
# Impute only columns with missing values, auto-decide strategies
df_imputed = universal_imputer(df, model="auto", verbose=True)
df_imputed.to_csv("data_imputed.csv", index=False)
