# app/nlp_pipeline.py

import langid
from deep_translator import GoogleTranslator

# ----------------------------
# 🌍 Language Detection
# ----------------------------
def detect_language(text: str) -> str:
    try:
        lang, _ = langid.classify(text)
        return lang
    except:
        return "en"

# ----------------------------
# 🌐 Translation
# ----------------------------
def translate_to_english(text: str, source_lang: str) -> str:
    if source_lang == "en":
        return text
    try:
        translated = GoogleTranslator(source=source_lang, target="en").translate(text)
        return translated
    except Exception as e:
        print(f"Translation failed: {e}")
        # fallback retry
        try:
            print("🔁 Retrying with auto language detection...")
            translated = GoogleTranslator(source='auto', target='en').translate(text)
            return translated
        except:
            return text

# ----------------------------
# 🔁 Optional: Back-translate response
# ----------------------------
def translate_to_original(text: str, target_lang: str) -> str:
    if target_lang == "en":
        return text
    try:
        translated = GoogleTranslator(source="en", target=target_lang).translate(text)
        return translated
    except Exception as e:
        print(f"Reverse translation failed: {e}")
        return text
    
import spacy
nlp_ner = spacy.load("en_core_web_sm")

def extract_entities(text: str) -> dict:
    doc = nlp_ner(text)
    entities = {}
    for ent in doc.ents:
        if ent.label_ not in entities:
            entities[ent.label_] = []
        entities[ent.label_].append(ent.text)
    return entities
