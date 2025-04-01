import streamlit as st
from transformers import MarianMTModel, MarianTokenizer
from typing import Tuple, Dict

@st.cache_resource
def get_translation_model(source_lang: str, target_lang: str) -> Tuple[MarianMTModel, MarianTokenizer]:
    """
    Çeviri modelini ve tokenizer'ı yükler.
    
    Args:
        source_lang: Kaynak dil kodu
        target_lang: Hedef dil kodu
        
    Returns:
        Tuple[MarianMTModel, MarianTokenizer]: Model ve tokenizer
    """
    model_id = f"Helsinki-NLP/opus-mt-{source_lang}-{target_lang}"
    print(f"Model indiriliyor: {source_lang} -> {target_lang}")
    model = MarianMTModel.from_pretrained(model_id)
    tokenizer = MarianTokenizer.from_pretrained(model_id)
    return model, tokenizer

class TranslationService:
    """Çeviri işlemlerini yöneten servis sınıfı."""
    
    # Desteklenen diller
    SUPPORTED_LANGUAGES = {
        'en': 'İngilizce',
        'de': 'Almanca',
        'fr': 'Fransızca',
        'es': 'İspanyolca',
        'it': 'İtalyanca',
        'ru': 'Rusça',
        'zh': 'Çince'
    }
    
    def __init__(self):
        """TranslationService sınıfını başlatır."""
        self._model_cache: Dict[str, MarianMTModel] = {}
        self._tokenizer_cache: Dict[str, MarianTokenizer] = {}
    
    def translate(self, text: str, source_lang: str, target_lang: str) -> str:
        """
        Metni bir dilden diğerine çevirir.
        
        Args:
            text: Çevrilecek metin
            source_lang: Kaynak dil kodu
            target_lang: Hedef dil kodu
            
        Returns:
            str: Çevrilmiş metin
        """
        try:
            return self._direct_translate(text, source_lang, target_lang)
        except Exception:
            return self._translate_via_english(text, source_lang, target_lang)
    
    def _direct_translate(self, text: str, source_lang: str, target_lang: str) -> str:
        """
        Direkt çeviri yapar.
        
        Args:
            text: Çevrilecek metin
            source_lang: Kaynak dil kodu
            target_lang: Hedef dil kodu
            
        Returns:
            str: Çevrilmiş metin
        """
        model, tokenizer = self._get_model(source_lang, target_lang)
        return self._translate_with_model(text, model, tokenizer)
    
    def _translate_via_english(self, text: str, source_lang: str, target_lang: str) -> str:
        """
        İngilizce üzerinden çeviri yapar.
        
        Args:
            text: Çevrilecek metin
            source_lang: Kaynak dil kodu
            target_lang: Hedef dil kodu
            
        Returns:
            str: Çevrilmiş metin
        """
        print(f"Direkt çeviri bulunamadı, İngilizce üzerinden çeviriliyor: {source_lang} -> en -> {target_lang}")
        intermediate = self._direct_translate(text, source_lang, 'en')
        return self._direct_translate(intermediate, 'en', target_lang)
    
    def _get_model(self, source_lang: str, target_lang: str) -> Tuple[MarianMTModel, MarianTokenizer]:
        """
        Çeviri modelini ve tokenizer'ı yükler veya önbellekten getirir.
        
        Args:
            source_lang: Kaynak dil kodu
            target_lang: Hedef dil kodu
            
        Returns:
            Tuple[MarianMTModel, MarianTokenizer]: Model ve tokenizer
        """
        model_id = f"Helsinki-NLP/opus-mt-{source_lang}-{target_lang}"
        
        if model_id not in self._model_cache:
            model, tokenizer = get_translation_model(source_lang, target_lang)
            self._model_cache[model_id] = model
            self._tokenizer_cache[model_id] = tokenizer
        
        return self._model_cache[model_id], self._tokenizer_cache[model_id]
    
    def _translate_with_model(self, text: str, model: MarianMTModel, tokenizer: MarianTokenizer) -> str:
        """
        Verilen model ve tokenizer ile çeviri yapar.
        
        Args:
            text: Çevrilecek metin
            model: Çeviri modeli
            tokenizer: Tokenizer
            
        Returns:
            str: Çevrilmiş metin
        """
        inputs = tokenizer(text, return_tensors="pt", padding=True)
        
        # Inference parametreleri:
        # outputs = model.generate(
        #     **inputs,
        #     max_length=128,          # Maksimum çeviri uzunluğu
        #     num_beams=4,             # Beam search için beam sayısı
        #     temperature=0.7,         # Çıktı çeşitliliği (0.0-1.0)
        #     top_k=50,                # En iyi k kelime seçimi
        #     top_p=0.95,              # Nucleus sampling
        #     repetition_penalty=1.2,   # Tekrar cezası
        #     length_penalty=1.0,       # Uzunluk cezası
        #     early_stopping=True       # Erken durdurma
        # )
        
        outputs = model.generate(**inputs, max_length=128)
        return tokenizer.decode(outputs[0], skip_special_tokens=True) 