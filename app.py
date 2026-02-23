from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({
        "message": "BMI Calculator Microservice is Running"
    })

@app.route('/bmi')
def calculate_bmi():
    try:
        weight = float(request.args.get('weight'))
        height = float(request.args.get('height'))

        if height <= 0 or weight <= 0:
            return jsonify({"error": "Height and Weight must be positive values"}), 400

        bmi = weight / (height ** 2)
        bmi = round(bmi, 2)

        if bmi < 18.5:
            category = "Underweight"
        elif 18.5 <= bmi < 24.9:
            category = "Normal"
        elif 25 <= bmi < 29.9:
            category = "Overweight"
        else:
            category = "Obese"

        return jsonify({
            "weight": weight,
            "height": height,
            "bmi": bmi,
            "category": category
        })

    except:
        return jsonify({"error": "Please provide weight and height parameters"}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)