import pandas as pd
import numpy as np

n_per_group = [334, 333, 333]  # Total = 1000

np.random.seed(42)

data = {
    'Jenis_Pupuk': ['organik'] * n_per_group[0] + ['kimia'] * n_per_group[1] + ['tanpa'] * n_per_group[2],
    'Tinggi_Tanaman': np.concatenate([
        np.random.normal(47, 2, n_per_group[0]),  
        np.random.normal(51, 2, n_per_group[1]),  
        np.random.normal(31, 2, n_per_group[2])   
    ])
}

df = pd.DataFrame(data)

df.to_csv('pupuk_tanaman.csv', index=False)
print("File pupuk_tanaman.csv dengan 1000 data telah dibuat!")
print(df.head())  