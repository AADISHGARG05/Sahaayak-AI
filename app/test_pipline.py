import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
# from nlp_pipeline import detect_language, translate_to_english

from app.nlp_pipeline import detect_language, translate_to_english

sample = "मुझे डॉक्टर की ज़रूरत है"
lang = detect_language(sample)
print(f"Detected language: {lang}")

translated = translate_to_english(sample, lang)
print(f"Translated: {translated}")


