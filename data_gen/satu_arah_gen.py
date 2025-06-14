import os
import numpy as np
import pandas as pd

# Regenerate the dataset
np.random.seed(42)
online = np.round(np.random.normal(loc=71, scale=2, size=334)).astype(int)
tatap_muka = np.round(np.random.normal(loc=85, scale=1.5, size=333)).astype(int)
mandiri = np.round(np.random.normal(loc=64, scale=1.5, size=333)).astype(int)

df = pd.DataFrame({
    'metode': ['Online'] * 334 + ['Tatap Muka'] * 333 + ['Mandiri'] * 333,
    'nilai': np.concatenate([online, tatap_muka, mandiri])
})

# Create directory in /mnt/data
output_dir = 'datasets'
os.makedirs(output_dir, exist_ok=True)

# Export CSV
csv_path = f'{output_dir}/satu_arah.csv'
df.to_csv(csv_path, index=False)