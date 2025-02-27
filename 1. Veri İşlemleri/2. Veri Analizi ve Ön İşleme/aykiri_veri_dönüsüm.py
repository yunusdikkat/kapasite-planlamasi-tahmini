import pandas as pd

# Verileri Yükleme 

df = pd.read_csv("sistem_verileri.csv")

# CPU kullanımı için aykırı değerleri ortalama ile değiştirme
cpu_ortalama = df['cpu_kullanimi'].mean()
df['cpu_kullanimi'] = df['cpu_kullanimi'].apply(lambda x: cpu_ortalama if x > 80 else x)

# Zaman damgasını datetime formatına dönüştür
df['zaman'] = pd.to_datetime(df['zaman'], unit='s')

# Zaman damgasını Unix timestamp'e dönüştür (saniye cinsinden)
df['zaman'] = df['zaman'].astype('int64') // 1e9

# Temiz verileri kaydetme
df.to_csv('temiz_sistem_verileri.csv', index=False)
