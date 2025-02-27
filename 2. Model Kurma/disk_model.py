import pandas as pd
from prophet import Prophet
import plotly.io as pio
import plotly.tools as tls

df = pd.read_csv('temiz_sistem_verileri.csv')
df = df.rename(columns={'zaman': 'ds'})
df['ds'] = pd.to_datetime(df['ds'],unit='s')

df = df[['ds', 'disk_kullanimi']]
df = df.rename(columns={'disk_kullanimi':'y'})

model= Prophet()
model.fit(df)

gelecek = model.make_future_dataframe(periods=30)
tahmin = model.predict(gelecek)

fig = model.plot(tahmin)
plotly_fig = tls.mpl_to_plotly(fig)
pio.show(plotly_fig)

fig2 = model.plot_components(tahmin)
plotly_fig2 = tls.mpl_to_plotly(fig2)
pio.show(plotly_fig2)
