import streamlit as st
import requests

def get_user_location():
    try:
        res = requests.get("http://ip-api.com/json/")
        data = res.json()
        return {
            "city": data.get("city"),
            "region": data.get("regionName"),
            "country": data.get("country"),
            "lat": data.get("lat"),
            "lon": data.get("lon")
        }
    except Exception as e:
        return {"error": str(e)}

# Local emergency numbers by country
emergency_numbers = {
    "India": {
        "Police": "100",
        "Ambulance": "102",
        "Fire": "101"
    },
    "USA": {
        "Police": "911",
        "Ambulance": "911",
        "Fire": "911"
    },
    "UK": {
        "Police": "999",
        "Ambulance": "999",
        "Fire": "999"
    },
    "Canada": {
        "Police": "911",
        "Ambulance": "911",
        "Fire": "911"
    }
}

# Page configuration
st.set_page_config(page_title="Sahaayak – Multilingual Emergency Assistant", page_icon="🏟")

# Title + Styling
st.markdown(
    """
    <h1 style='text-align: center; color: #007ACC;'>🏟 Sahaayak</h1>
    <h3 style='text-align: center; color: gray;'>Your Multilingual Emergency Assistant Bot</h3>
    <hr style="margin-top: 0">
    """,
    unsafe_allow_html=True
)

# Input Section
with st.form("intent_form"):
    user_input = st.text_input(
        "🗣️ Enter your emergency message (in any language)",
        placeholder="Type here in English, Hindi, Marathi, Tamil, etc...",
        label_visibility="visible"
    )
    submit = st.form_submit_button("🚨 Send Emergency Request")

# API Call + Response
if submit and user_input.strip() != "":
    with st.spinner("Processing your request..."):
        try:
            # Step 1: Location Detection
            location = get_user_location()

            # Step 2: API Call to FastAPI backend
            response = requests.post("http://127.0.0.1:8000/predict_intent/", json={"text": user_input})

            if response.status_code == 200:
                result = response.json()

                # Sidebar Location Info
                with st.sidebar:
                    st.markdown("## 📍 Your Location")
                    if "error" in location:
                        st.error("Could not detect location.")
                    else:
                        st.success("Location detected")
                        st.write(f"**City:** {location['city']}")
                        st.write(f"**Region:** {location['region']}")
                        st.write(f"**Country:** {location['country']}")
                        st.write(f"**Coordinates:** {location['lat']}, {location['lon']}")

                        # Google Maps Links
                        lat, lon = location['lat'], location['lon']
                        hospital_url = f"https://www.google.com/maps/search/hospital/@{lat},{lon},15z"
                        police_url = f"https://www.google.com/maps/search/police+station/@{lat},{lon},15z"
                        fire_url = f"https://www.google.com/maps/search/fire+station/@{lat},{lon},15z"

                        st.markdown("### 🗽️ Nearby Emergency Services")
                        st.markdown(f"- 🏥 [Hospitals Near You]({hospital_url})", unsafe_allow_html=True)
                        st.markdown(f"- 🚓 [Police Stations Near You]({police_url})", unsafe_allow_html=True)
                        st.markdown(f"- 🔥 [Fire Stations Near You]({fire_url})", unsafe_allow_html=True)

                        # Emergency Numbers
                        st.markdown("### ☎️ Emergency Numbers")
                        user_country = location.get("country", "Unknown")
                        if user_country in emergency_numbers:
                            numbers = emergency_numbers[user_country]
                            st.write(f"**Country Detected:** {user_country}")
                            for service, number in numbers.items():
                                st.markdown(f"- **{service}**: 📞 `{number}`")
                        else:
                            st.warning("⚠️ Emergency numbers not found for your country.")

                # Main Result
                st.markdown("---")
                st.markdown("### 🧠 Prediction Result")
                st.markdown(f"<b>🌐 Language:</b> {result['language']}", unsafe_allow_html=True)
                st.markdown(f"<b>🔁 Translated Text:</b> {result['translated_text']}", unsafe_allow_html=True)
                st.markdown(f"<b>🎯 Detected Intent:</b> <span style='color:green'>{result['intent']}</span>", unsafe_allow_html=True)

                st.markdown(
                    f"""
                    <b>💬 Bot Response:</b><br>
                    <div style='
                        background-color: rgba(255, 255, 255, 0.05);
                        padding: 12px 15px;
                        border-radius: 10px;
                        margin-top: 5px;
                        color: white;
                        font-size: 16px;
                    '>{result['response']}</div>
                    """,
                    unsafe_allow_html=True
                )

                # NER Entities
                if result.get("entities"):
                    st.markdown("### 🔍 Extracted Entities")
                    for label, values in result["entities"].items():
                        st.markdown(f"**{label}**: {', '.join(values)}")

                # Emergency Action Buttons
                st.markdown("### 🚨 Emergency Actions")
                intent = result['intent']
                numbers = emergency_numbers.get(user_country, {})

                if intent == "medical_help":
                    if st.button("🚑 Call Ambulance"):
                        st.info(f"Dial: 📞 {numbers.get('Ambulance', 'Not Available')}")
                        st.markdown(f"[🗽 Nearby Hospitals](https://www.google.com/maps/search/hospital/@{lat},{lon},15z)", unsafe_allow_html=True)

                elif intent == "fire_emergency":
                    if st.button("🔥 Report Fire"):
                        st.info(f"Dial: 📞 {numbers.get('Fire', 'Not Available')}")
                        st.markdown(f"[🛰️ Nearby Fire Stations](https://www.google.com/maps/search/fire+station/@{lat},{lon},15z)", unsafe_allow_html=True)

                elif intent == "police_assistance":
                    if st.button("🚓 Contact Police"):
                        st.info(f"Dial: 📞 {numbers.get('Police', 'Not Available')}")
                        st.markdown(f"[🚓 Nearby Police Stations](https://www.google.com/maps/search/police+station/@{lat},{lon},15z)", unsafe_allow_html=True)

                else:
                    st.info("ℹ️ No direct emergency action available for this intent.")

            else:
                st.error(f"❌ API returned status code {response.status_code}")

        except Exception as e:
            st.error(f"⚠️ Error: {e}")


# run this
# python -m streamlit run streamlit_app.py