import pandas as pd
from prophet import Prophet
import plotly.io as pio
import plotly.tools as tls

# Verileri yükle
df = pd.read_csv('temiz_sistem_verileri.csv')
# Zaman damgası sütununun adını 'ds' olarak değiştir
df = df.rename(columns={'zaman': 'ds'})
# Zaman damgalarını datetime nesnelerine dönüştür
df['ds'] = pd.to_datetime(df['ds'], unit='s')

# Prophet için veri formatını düzenle
df = df[['ds', 'cpu_kullanimi']]  # Sadece ds ve cpu_kullanimi sütunlarını seç
df = df.rename(columns={'cpu_kullanimi': 'y'})  # cpu_kullanimi sütununu y olarak yeniden adlandır

# Prophet modelini oluştur ve eğit
model = Prophet()  # datetime_unit parametresini kullanmayın
model.fit(df)

# Gelecek 30 gün için tahmin yap
gelecek = model.make_future_dataframe(periods=30)  # 30 günlük tahmin
tahmin = model.predict(gelecek)

# Tahmin sonuçlarını görselleştir
fig = model.plot(tahmin)
plotly_fig = tls.mpl_to_plotly(fig)  # Matplotlib figürünü Plotly figürüne dönüştür
pio.show(plotly_fig)  # Plotly figürünü görüntüle

# Tahmin bileşenlerini görselleştir
fig2 = model.plot_components(tahmin)
plotly_fig2 = tls.mpl_to_plotly(fig2)  # Matplotlib figürünü Plotly figürüne dönüştür
pio.show(plotly_fig2)  # Plotly figürünü görüntüle