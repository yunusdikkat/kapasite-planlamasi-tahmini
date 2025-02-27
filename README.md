# Kapasite Planlaması Tahmini

Bu proje, sistem kaynaklarının (CPU, bellek, disk) kullanımını tahmin etmek için bir makine öğrenmesi modeli eğitmeyi amaçlamaktadır. Sistem performansını izlemek ve gelecekteki kaynak ihtiyaçlarını tahmin etmek için kullanılabilir.

## Proje Adımları:

Veri Toplama: Sistem kaynaklarının kullanım verileri, belirli aralıklarla toplanır ve bir CSV dosyasına kaydedilir.    
Veri İşleme: Toplanan veriler, makine öğrenmesi modeli için uygun hale getirilir. Bu adımda, aykırı değerler tespit edilir ve dönüştürülür, veriler analiz edilir ve görselleştirilir.    
Model Eğitimi: İşlenmiş veriler kullanılarak bir makine öğrenmesi modeli eğitilir. Bu projede, CPU, bellek ve disk kullanımı için ayrı ayrı modeller eğitilir.    
Model Değerlendirmesi: Eğitilen modellerin performansı, test verileri kullanılarak değerlendirilir.    
Tahmin: Eğitilen modeller, gelecekteki sistem kaynaklarının kullanımını tahmin etmek için kullanılır.    
Kullanılan Teknolojiler:

Python
Pandas
Scikit-learn
Dosya Yapısı:

1. Veri İşlemleri: Veri toplama ve işleme adımlarını içerir.
1. Veri Oluşturma: Veri toplama betiklerini ve toplanan ham verileri içerir.
2. Veri Analizi ve Ön İşleme: Veri analizi ve ön işleme betiklerini içerir.
2. Model Kurma: Model eğitimi ve değerlendirmesi adımlarını içerir.
cpu_model.py: CPU kullanımı için model eğitimi betiği.
bellek_model.py: Bellek kullanımı için model eğitimi betiği.
disk_model.py: Disk kullanımı için model eğitimi betiği.
3. Tahmin: Tahmin adımlarını içerir.
## Kullanım:

veri_toplama.py betiğini kullanarak sistem kaynaklarının kullanım verilerini toplayın.
aykiri_veri_tespit.py ve aykiri_veri_dönüsüm.py betiklerini kullanarak aykırı değerleri tespit edin ve dönüştürün.
grafik.py betiğini kullanarak verileri görselleştirin.
cpu_model.py, bellek_model.py ve disk_model.py betiklerini kullanarak CPU, bellek ve disk kullanımı için modeller eğitin.
Eğitilen modelleri kullanarak gelecekteki sistem kaynaklarının kullanımını tahmin edin.
## Notlar:

Proje, Python 3.x sürümü ile uyumludur.
Proje, Pandas ve Scikit-learn kütüphanelerini kullanır. Bu kütüphaneleri yüklemek için pip install pandas scikit-learn komutunu kullanabilirsiniz.
Proje, sistem kaynaklarının kullanım verilerini sistem_verileri.csv dosyasına kaydeder.
