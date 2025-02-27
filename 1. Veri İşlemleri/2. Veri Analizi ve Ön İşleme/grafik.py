import pandas as pd
import matplotlib.pyplot as plt

# Verileri yükle
df = pd.read_csv('sistem_verileri.csv')

# Zaman damgasını datetime formatına dönüştür
df['zaman'] = pd.to_datetime(df['zaman'], unit='s')

# Zaman serisi grafikleri
plt.figure(figsize=(12, 8))

plt.subplot(3, 1, 1)
plt.plot(df['zaman'], df['cpu_kullanimi'])
plt.title('CPU Kullanımı')

plt.subplot(3, 1, 2)
plt.plot(df['zaman'], df['bellek_kullanimi'])
plt.title('Bellek Kullanımı')

plt.subplot(3, 1, 3)
plt.plot(df['zaman'], df['disk_kullanimi'])
plt.title('Disk Kullanımı')

plt.tight_layout()
plt.show()

# Histogram
plt.figure(figsize=(12, 4))

plt.subplot(1, 3, 1)
plt.hist(df['cpu_kullanimi'])
plt.title('CPU Kullanımı')

plt.subplot(1, 3, 2)
plt.hist(df['bellek_kullanimi'])
plt.title('Bellek Kullanımı')

plt.subplot(1, 3, 3)
plt.hist(df['disk_kullanimi'])
plt.title('Disk Kullanımı')

plt.tight_layout()
plt.show()