# 🧠 Insurance Premium Prediction API

A **FastAPI-based Machine Learning API** that predicts insurance premium charges based on user details like age, BMI, smoking status, and more. The model is trained and served through a high-performance backend with real-time predictions.

> 🔗 **Live API Docs:** [http://16.170.238.125:8000/docs](http://16.170.238.125:8000/docs)

---

## 🚀 Features

- 💡 Predict insurance premiums instantly via API
- ⚡ Built with FastAPI for high-speed inference
- 📊 Machine Learning model trained using real-world data
- ✅ Input validation with Pydantic
- 🌐 Live deployed API (see link above)

---

## 🛠️ Tech Stack

- **Backend:** FastAPI, Uvicorn
- **ML Model:** Scikit-learn
- **Languages:** Python 3.8+
- **Other:** Pandas, NumPy, Pydantic
- **Deployment:** Public IP server (EC2 or similar)

---

## 📁 Project Structure

```text
Insurance-Premium-prediction/
│
├── __pycache__/              # Python bytecode cache (auto-generated)
├── config/                   # Configuration settings (e.g., file paths, constants)
├── model/                    # Trained ML model, loading & prediction logic
├── myenv/                    # Local virtual environment (should be in .gitignore)
├── schema/                   # Pydantic models for request/response validation
│
├── app.py                    # Main FastAPI application file
├── Dockerfile                # Docker configuration for containerization
└── requirements.txt          # Python dependencies for the project
```

## 2. Create and Activate Virtual Environment
- python -m venv venv
- source venv/bin/activate  # Windows: venv\Scripts\activate

## 3. Install Dependencies
- pip install -r requirements.txt

## ▶️ Run the API Locally
- uvicorn app:app --reload
- Now visit: http://127.0.0.1:8000/docs

## 🌐 Live API
- Deployed and accessible at:
- 📍 http://16.170.238.125:8000/docs

🙌 Author
Vikash Bharti
      🔗 GitHub: neuroCodexAI

Contact: https://neurocodexai.github.io/ 
