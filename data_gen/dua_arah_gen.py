import os
import numpy as np
import pandas as pd
from itertools import product

# Regenerate the dataset for two-way ANOVA
np.random.seed(42)
metode = ['Online', 'Tatap Muka', 'Mandiri']
waktu = ['Pagi', 'Malam']
n_samples = 150

data = []
for m, w in product(metode, waktu):
    if m == 'Online':
        if w == 'Pagi':
            nilai = np.round(np.random.normal(
                loc=70, scale=2, size=n_samples)).astype(int)
        else:
            nilai = np.round(np.random.normal(
                loc=72, scale=2.5, size=n_samples)).astype(int)
    elif m == 'Tatap Muka':
        if w == 'Pagi':
            nilai = np.round(np.random.normal(
                loc=86, scale=1.5, size=n_samples)).astype(int)
        else:
            nilai = np.round(np.random.normal(
                loc=84, scale=1.8, size=n_samples)).astype(int)
    else:  # Mandiri
        if w == 'Pagi':
            nilai = np.round(np.random.normal(
                loc=65, scale=1.5, size=n_samples)).astype(int)
        else:
            nilai = np.round(np.random.normal(
                loc=63, scale=1.7, size=n_samples)).astype(int)
    data.append(pd.DataFrame(
        {'metode': [m] * n_samples, 'waktu': [w] * n_samples, 'nilai': nilai}))

df_2arah = pd.concat(data)

# Create directory in /mnt/data
output_dir = 'datasets'
os.makedirs(output_dir, exist_ok=True)

# Export CSV for two-way ANOVA
csv_path_2arah = f'{output_dir}/dua_arah.csv'
df_2arah.to_csv(csv_path_2arah, index=False)

print(f"Data untuk ANOVA dua arah telah disimpan di: {csv_path_2arah}")
