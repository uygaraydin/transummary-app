# 🌐 Çeviri ve Özetleme Uygulaması

Bu proje, metinleri farklı dillere çevirmenize ve özetlemenize olanak sağlayan basit bir web uygulamasıdır.

## 🚀 Özellikler

- 7 farklı dil desteği
- Direkt dil çiftleri arasında çeviri (örn: Almanca -> Fransızca)
- Desteklenmeyen dil çiftleri için İngilizce üzerinden çeviri (örn: İspanyolca -> Çince)
- Otomatik metin özetleme
- Kullanıcı dostu arayüz
- Model önbellekleme ile hızlı çeviri

## 🛠️ Teknolojiler

- Streamlit (Web arayüzü)
- Hugging Face Transformers (AI/ML modelleri)
- PyTorch (Derin öğrenme framework'ü)
- BART-large-CNN (Özetleme modeli)
- Helsinki-NLP OPUS-MT (Çeviri modelleri)
- Prompt Engineering (Model performans optimizasyonu)

## 🤖 Kullanılan AI Modelleri

### Çeviri Modelleri
- **Helsinki-NLP OPUS-MT**: Çok dilli çeviri modelleri
  - Direkt dil çiftleri için özel modeller
  - İngilizce üzerinden çeviri için ara modeller
  - Hugging Face Hub üzerinden otomatik indirme ve önbellekleme

### Özetleme Modeli
- **Facebook BART-large-CNN**: Metin özetleme modeli
  - CNN veri seti üzerinde eğitilmiş
  - Yüksek kaliteli özetler
  - Hugging Face pipeline ile kolay entegrasyon

## 📦 Kurulum

1. Gerekli paketleri yükleyin:
```bash
pip install -r requirements.txt
```

2. Uygulamayı başlatın:
```bash
streamlit run translator_app.py
```

## 🌍 Desteklenen Diller

### Çeviri Dilleri
- İngilizce (en)
- Almanca (de)
- Fransızca (fr)
- İspanyolca (es)
- İtalyanca (it)
- Rusça (ru)
- Çince (zh)

### Çeviri Özellikleri
- Direkt çeviri: İngilizce ile diğer diller arasında
- İki adımlı çeviri: Desteklenmeyen dil çiftleri için İngilizce üzerinden çeviri
  - Örnek: İspanyolca -> Çince çevirisi için:
    1. İspanyolca -> İngilizce
    2. İngilizce -> Çince

## 📁 Proje Yapısı

```
.
├── translator_app.py    # Ana uygulama
├── services/           # Servis modülleri
│   ├── __init__.py    # Paket başlatıcı
│   ├── translation_service.py    # Çeviri servisi
│   └── summarization_service.py  # Özetleme servisi
└── requirements.txt    # Gerekli kütüphaneler
```

## 🏗️ Mimari

Proje, aşağıdaki tasarım prensiplerini takip eder:

- **Modüler Yapı**: Her servis kendi sorumluluğuna sahip
- **SOLID Prensipleri**: Tek Sorumluluk ve Açık/Kapalı prensipleri
- **Dependency Injection**: Servisler bağımsız olarak enjekte edilebilir
- **Caching**: Modeller önbelleğe alınır ve tekrar kullanılır
- **Hugging Face Entegrasyonu**: Modern AI/ML pratikleri

## 👤 Yazar

Uygar Aydın

## 🙏 Teşekkürler

- [Helsinki-NLP](https://huggingface.co/Helsinki-NLP) - Çeviri modelleri
- [Facebook](https://huggingface.co/facebook/bart-large-cnn) - Özetleme modeli
- [Hugging Face](https://huggingface.co) - AI/ML altyapısı ve modeller
