import psutil
import time
import csv

def verileri_topla():
  """Sistem ve ağ bilgilerini toplar ve CSV dosyasına yazar."""

  with open('sistem_verileri.csv', 'w', newline='') as csvfile:
    alanlar = ['zaman', 'cpu_kullanimi', 'bellek_kullanimi', 'disk_kullanimi']
    yazici = csv.DictWriter(csvfile, fieldnames=alanlar)
    yazici.writeheader()

    while True:
      cpu_yuzdesi = psutil.cpu_percent()
      bellek = psutil.virtual_memory()
      disk = psutil.disk_usage('/')

      yazici.writerow({
          'zaman': time.time(),
          'cpu_kullanimi': cpu_yuzdesi,
          'bellek_kullanimi': bellek.percent,
          'disk_kullanimi': disk.percent
      })

      time.sleep(20)  # Her 20 saniyede bir veri topla

if __name__ == "__main__":
  verileri_topla()