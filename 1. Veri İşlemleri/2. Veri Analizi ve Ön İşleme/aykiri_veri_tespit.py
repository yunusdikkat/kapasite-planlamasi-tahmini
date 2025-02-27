import pandas as pd
import matplotlib.pyplot as plt

# Verileri yükle
df = pd.read_csv('sistem_verileri.csv')

# Zaman damgasını datetime formatına dönüştür
df['zaman'] = pd.to_datetime(df['zaman'], unit='s')

# Metrikler için box plot grafikleri
metrikler = ['cpu_kullanimi', 'bellek_kullanimi', 'disk_kullanimi']

plt.figure(figsize=(12, 8))
for i, metrik in enumerate(metrikler):
    plt.subplot(len(metrikler), 1, i + 1)
    plt.boxplot(df[metrik])
    plt.title(f'{metrik.capitalize()} Box Plot')

plt.tight_layout()
plt.show()