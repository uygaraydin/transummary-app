import streamlit as st
from services import TranslationService, SummarizationService

# Sayfa yapılandırması
st.set_page_config(
    page_title="Çeviri ve Özetleme Uygulaması",
    page_icon="🌐",
    layout="wide"
)

# Servisleri başlat
@st.cache_resource
def get_translation_service():
    return TranslationService()

@st.cache_resource
def get_summarization_service():
    return SummarizationService()

# Başlık
st.title("🌐 Çeviri ve Özetleme Uygulaması")

# Session state başlatma
if 'source_lang' not in st.session_state:
    st.session_state.source_lang = 'en'
if 'target_lang' not in st.session_state:
    st.session_state.target_lang = 'de'
if 'input_text' not in st.session_state:
    st.session_state.input_text = ""
if 'translated_text' not in st.session_state:
    st.session_state.translated_text = ""
if 'summary' not in st.session_state:
    st.session_state.summary = ""

# Dil seçimi
col1, col2 = st.columns(2)

with col1:
    source_lang = st.selectbox(
        "Kaynak Dil",
        options=list(TranslationService.SUPPORTED_LANGUAGES.keys()),
        format_func=lambda x: TranslationService.SUPPORTED_LANGUAGES[x],
        key='source_lang'
    )

with col2:
    target_lang = st.selectbox(
        "Hedef Dil",
        options=list(TranslationService.SUPPORTED_LANGUAGES.keys()),
        format_func=lambda x: TranslationService.SUPPORTED_LANGUAGES[x],
        key='target_lang'
    )

# Metin girişi
input_text = st.text_area(
    "Çevrilecek Metin",
    value=st.session_state.input_text,
    height=150
)

# Butonlar
col1, col2 = st.columns(2)

with col1:
    if st.button("Çevir", type="primary"):
        if input_text:
            with st.spinner("Çeviri yapılıyor..."):
                translation_service = get_translation_service()
                st.session_state.translated_text = translation_service.translate(
                    input_text,
                    source_lang,
                    target_lang
                )
                st.session_state.input_text = input_text

with col2:
    if st.button("Özetle"):
        if st.session_state.translated_text:
            with st.spinner("Özetleniyor..."):
                summarization_service = get_summarization_service()
                st.session_state.summary = summarization_service.summarize(
                    st.session_state.translated_text
                )

# Sonuçlar
if st.session_state.translated_text:
    st.subheader("Çeviri Sonucu")
    st.write(st.session_state.translated_text)

if st.session_state.summary:
    st.subheader("Özet")
    st.write(st.session_state.summary)
