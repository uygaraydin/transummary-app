import streamlit as st
from transformers import pipeline
from typing import Optional

@st.cache_resource
def get_summarizer() -> pipeline:
    """
    Özetleme modelini yükler.
    
    Returns:
        pipeline: Özetleme modeli
    """
    print("Özetleme modeli indiriliyor")
    return pipeline("summarization", model="facebook/bart-large-cnn")

class SummarizationService:
    """Özetleme işlemlerini yöneten servis sınıfı."""
    
    def __init__(self):
        """SummarizationService sınıfını başlatır."""
        self._summarizer: Optional[pipeline] = None
    
    def summarize(self, text: str, max_length: int = 130, min_length: int = 30) -> str:
        """
        Metni özetler.
        
        Args:
            text: Özetlenecek metin
            max_length: Özetin maksimum uzunluğu
            min_length: Özetin minimum uzunluğu
            
        Returns:
            str: Özetlenmiş metin
        """
        summarizer = self._get_summarizer()
        
        # Inference parametreleri:
        # summary = summarizer(
        #     text,
        #     max_length=130,          # Maksimum özet uzunluğu
        #     min_length=30,           # Minimum özet uzunluğu
        #     do_sample=True,          # Rastgele örnekleme
        #     temperature=0.7,         # Çıktı çeşitliliği
        #     top_k=50,                # En iyi k kelime seçimi
        #     top_p=0.95,              # Nucleus sampling
        #     repetition_penalty=1.2,   # Tekrar cezası
        #     length_penalty=1.0,       # Uzunluk cezası
        #     early_stopping=True       # Erken durdurma
        # )
        
        summary = summarizer(text, max_length=max_length, min_length=min_length, do_sample=False)
        return summary[0]['summary_text']
    
    def _get_summarizer(self) -> pipeline:
        """
        Özetleme modelini yükler veya önbellekten getirir.
        
        Returns:
            pipeline: Özetleme modeli
        """
        if self._summarizer is None:
            self._summarizer = get_summarizer()
        return self._summarizer 