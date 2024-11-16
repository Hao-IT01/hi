import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("AppleStore.csv")
df_max_scaled = df[
    ["rating_count_tot", "rating_count_ver"]
]  # take two columns "rating_count_tot", "rating_count_ver" for normalization

# apply normalization techniques - max-abs scaling.
for column in df_max_scaled.columns:
    df_max_scaled[column] = df_max_scaled[column] / df_max_scaled[column].abs().max()

print(df_max_scaled)
