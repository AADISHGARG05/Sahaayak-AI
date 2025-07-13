# 🛟 Sahaayak – A Multilingual Emergency Assistant Bot

> ⚡ Empowering citizens with AI-based emergency support in **any language**  
> 🚨 Built with FastAPI, NLP, NER, and a multilingual Streamlit frontend.

---

## 📌 Project Overview

**Sahaayak** is an AI-powered multilingual assistant designed to help people during emergencies by:
- Understanding messages in **any Indian/local language**
- Detecting the **emergency intent** (e.g., fire, medical, police)
- Extracting critical entities like **locations** or **names**
- Detecting the user’s **live location** via IP
- Displaying **local emergency numbers**
- Recommending nearest **hospitals, police stations**, or **fire services**

---

## 🚀 Key Features

| Feature                        | Description                                                                 |
|-------------------------------|-----------------------------------------------------------------------------|
| 🧠 **Multilingual NLP**        | Detects language and translates input into English internally.             |
| 🔍 **Intent Detection**        | Uses trained ML models to classify the emergency type.                     |
| 🗺️ **Location Detection**     | Auto-detects user's IP-based location for contextual help.                |
| 📌 **NER Extraction**          | Identifies entities like names, locations, etc.                            |
| 🌐 **FastAPI Backend**         | Provides a powerful, flexible backend for predictions.                     |
| 💬 **Streamlit Frontend**      | Clean, dark-themed UI for interaction in real time.                        |
| ☎️ **Emergency Numbers**       | Displays country-specific emergency contact numbers.                       |
| 📍 **Map Integration**         | Shows nearby emergency service routes via Google Maps.                     |
| 🧪 **Test Examples**           | Sample texts provided in multiple Indian languages.                        |

---

## 📂 Project Structure

Sahaayak/
├── app/ # FastAPI backend (intent logic, NER, etc.)
│ ├── main.py
│ ├── predict_intent.py
│ ├── nlp_pipeline.py
│ └── ...
├── streamlit_app.py # Multilingual frontend using Streamlit
├── models/ # Pretrained models (intent classification, etc.)
├── data/ # Sample input data or supporting language files
├── sample_text.txt # Test messages in various languages
├── notebooks/ # Jupyter notebooks (EDA, training logs)
├── requirements.txt # Project dependencies
└── README.md # You're reading it!

---

## 🧠 Tech Stack

- **Programming Language:** Python 3.9+
- **Frontend UI:** Streamlit
- **Backend API:** FastAPI
- **NLP:** `langdetect`, `transformers`, `NER via spaCy`
- **Deployment Ready:** Uvicorn for FastAPI, local Streamlit runner
- **Others:** Requests, IP Geolocation API, Google Maps URLs

---

## 🔧 Installation & Setup

### ✅ Step 1: Clone the Repository
```bash
git clone https://github.com/your-username/Sahaayak-AI.git
cd Sahaayak-AI
```
### ✅ Step 3: Run the FastAPI Backend
```bash
cd app
uvicorn main:app --reload
```
###### Access API at: http://127.0.0.1:8000/docs

### ✅ Step 4: Run the Streamlit Frontend
```bash
streamlit run streamlit_app.py
```

## 🧪 Sample Multilingual Texts

Paste these in the UI to test multilingual capabilities:

| Language | Input |
|----------|-------|
| Hindi    | "मुझे पुलिस की मदद चाहिए" |
| Marathi  | "माझ्या परिसरात आग लागली आहे" |
| Tamil    | "எனக்கு மருத்துவ உதவி தேவை" |
| Bengali  | "আমার আগুন লাগার সাহায্য দরকার" |
| English  | "There is a fire in my neighborhood" |

---

## 🗺️ Google Maps Integration

The app auto-generates nearby service links:

- [🏥 Hospitals](https://www.google.com/maps/search/hospital)
- [🚓 Police Stations](https://www.google.com/maps/search/police+station)
- [🔥 Fire Stations](https://www.google.com/maps/search/fire+station)

---

## 💡 Future Improvements

- 🔒 JWT-based user session for secure use  
- 🧭 Real-time geolocation (using browser APIs)  
- 📱 Convert to PWA/mobile-friendly app  
- 📊 Analytics dashboard for authority alerts  

---

## 🤝 Acknowledgements

- [FastAPI](https://fastapi.tiangolo.com/)
- [Streamlit](https://streamlit.io/)
- [spaCy](https://spacy.io/)
- [Transformers by HuggingFace](https://huggingface.co/)
- [ip-api.com](http://ip-api.com/) – Free IP geolocation API

---

## 📣 Contact

**AADISH GARG**  
🔗 [GitHub](https://github.com/AADISHGARG05)  
🔗 [LinkedIn](https://www.linkedin.com/in/aadish-garg-ab2a59288/)
