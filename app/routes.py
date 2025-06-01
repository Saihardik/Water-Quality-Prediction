from flask import Blueprint, request, jsonify, render_template
from app.ml_model import load_model

main = Blueprint('main', __name__)
model = load_model()

@main.route('/')
def home():
    return render_template("form.html")

@main.route('/predict', methods=['POST'])
def predict():
    try:
        from app.ml_model import load_model
        model = load_model()  # ✅ Load inside the route

        input_data = [
            float(request.form['ph']),
            float(request.form['Hardness']),
            float(request.form['Sulfate']),
            float(request.form['Conductivity']),
            float(request.form['Organic_carbon']),
            float(request.form['Trihalomethanes']),
            float(request.form['Turbidity'])
        ]

        prediction = model.predict([input_data])[0]
        result = "Safe" if prediction == 1 else "Not Safe"

        return render_template("form.html", prediction=result)

    except Exception as e:
        return render_template("form.html", error=str(e))