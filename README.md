# 💧 WaterNet: Water Quality Prediction Using Machine Learning

WaterNet is an intelligent web application designed to predict the **potability** (drinkability) of water based on its **physicochemical properties**. Built with Flask and powered by a trained machine learning model (Random Forest), the system simulates a real-time monitoring dashboard without requiring physical sensors.

---

## 🚀 Features

- 🌐 Web-based UI to input water quality parameters
- 🔍 Predicts whether water is **Safe** or **Not Safe**
- 📊 Trained on real-world physicochemical datasets
- 🧠 Uses Random Forest Classifier for prediction
- ✅ Ideal for low-resource environments or education

---

## 📂 Project Structure

```
WaterNet/
├── run.py                      # Flask app entry point
├── app/
│   ├── __init__.py             # Flask app factory
│   ├── routes.py               # Routes for UI and prediction
│   └── ml_model.py             # Model training & loading logic
├── dataset/
│   └── water_quality.csv       # Training dataset
├── models/
│   └── model.pkl               # Trained ML model (Random Forest)
├── templates/
│   └── form.html               # HTML UI for user input
├── static/
│   └── style.css               # CSS styling (Bootstrap or custom)
├── requirements.txt            # Python dependencies
└── WaterNet_Final_Report.docx  # 📄 Full project report
```

---

## 🧠 Machine Learning Model

- **Model Used**: `RandomForestClassifier` from scikit-learn
- **Training Accuracy**: Balanced and evaluated
- **Target Variable**: `Potability` (1 = Safe, 0 = Not Safe)
- **Key Features**:
  - `pH`
  - `Hardness`
  - `Sulfate`
  - `Conductivity`
  - `Organic Carbon`
  - `Trihalomethanes`
  - `Turbidity`

---

## 📈 Input Feature Importance (Sample)

| Feature            | Typical Impact |
|--------------------|----------------|
| Sulfate            | ⭐⭐⭐⭐           |
| Conductivity       | ⭐⭐⭐⭐           |
| pH                 | ⭐⭐⭐            |
| Turbidity          | ⭐⭐             |
| Organic Carbon     | ⭐⭐             |

---

## 🛠️ How to Run Locally

1. Clone the repo:
   ```bash
   git clone https://github.com/YOUR_USERNAME/WaterNet.git
   cd WaterNet
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Train the model (optional):
   ```bash
   python -c "from app.ml_model import train_and_save_model; train_and_save_model()"
   ```

4. Run the server:
   ```bash
   python run.py
   ```

5. Open your browser and go to:
   ```
   http://127.0.0.1:5000/
   ```

---

## 📄 Project Report

> The detailed project documentation and explanation of features, ML model, dataset, and flowcharts can be found in the DOCX report:
📎 [`WaterNet_Final_Report.docx`](WaterNet_Final_Report.docx)

---

## 👨‍💻 Developed by

**Sai Harsha**  
Project Title: *WaterNet — A Network for Monitoring and Assessing Water Quality*

---

## ⭐ License

This project is for educational purposes only. For commercial or research use, please cite the source or contact the author.
