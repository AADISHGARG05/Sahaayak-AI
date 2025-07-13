import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app.predict_intent import predict_user_intent

sample_input = "मुझे डॉक्टर चाहिए"
result = predict_user_intent(sample_input)

print("\n🔍 Prediction Result:")
for k, v in result.items():
    print(f"{k}: {v}")