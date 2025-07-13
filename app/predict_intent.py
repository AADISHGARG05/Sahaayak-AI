import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import joblib
from app.nlp_pipeline import detect_language, translate_to_english, translate_to_original
from app.nlp_pipeline import extract_entities

# Load model and vectorizer
model = joblib.load("models/intent_model.pkl")
vectorizer = joblib.load("models/vectorizer.pkl")

# Sample intent-response map
INTENT_RESPONSES = {
    "medical_help": "Please stay calm. Medical help is on the way.",
    "fire_emergency": "Evacuate immediately. Fire services are being notified.",
    "police_assistance": "Police assistance is being dispatched. Stay safe.",
    "lost_person": "We’ve noted your report. Search and rescue is being initiated.",
    "natural_disaster": "Please move to a safe location. Authorities have been informed.",
    "other_emergency": "Emergency services are being alerted. Help is on the way."
}

# -------------------------------
# 🔮 Main Prediction Pipeline
# -------------------------------
def predict_user_intent(user_input: str) -> dict:
    # 1. Detect language
    detected_lang = detect_language(user_input)
    
    # 2. Translate to English
    translated_text = translate_to_english(user_input, detected_lang)

    # 3. Vectorize and Predict
    vectorized = vectorizer.transform([translated_text])
    predicted_intent = model.predict(vectorized)[0]

    # 4. Generate Response (EN)
    response_en = INTENT_RESPONSES.get(predicted_intent, "Sorry, we couldn’t understand the emergency.")

    entities = extract_entities(translated_text)

    # 5. Translate back to user's language (if needed)
    final_response = translate_to_original(response_en, detected_lang)

    return {
        "original_text": user_input,
        "language": detected_lang,
        "translated_text": translated_text,
        "intent": predicted_intent,
        "entities": entities,
        "response": final_response

    }