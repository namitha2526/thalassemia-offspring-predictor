from flask import Flask, request, jsonify
from flask_cors import CORS
import numpy as np
import joblib

app = Flask(__name__)
CORS(app, resources={r"/api/*": {"origins": "http://localhost:5173"}})

model = joblib.load('thalassemia_model.joblib')
scaler = joblib.load('thalassemia_scaler.joblib')
label_encoder = joblib.load('thalassemia_label_encoder.joblib')

# Define valid ranges for input features
INPUT_RANGES = {
    'mother_age': (20, 45),
    'father_age': (20, 45),
    'mother_Hb': (8, 15),
    'father_Hb': (8, 15),
    'mother_HbA2': (1, 10),
    'father_HbA2': (1, 10),
    'mother_HbF': (0, 10),
    'father_HbF': (0, 10),
    'mother_MCV': (50, 100),
    'father_MCV': (50, 100),
    'mother_MCH': (27, 34),
    'father_MCH': (27, 34),
    'mother_RBC': (3.8, 5.5),
    'father_RBC': (3.8, 5.5),
    'mother_RDW': (11.5, 14.5),
    'father_RDW': (11.5, 14.5)
}

def validate_inputs(inputs):
    """Validate input values against defined ranges."""
    errors = []
    for field, value in inputs.items():
        min_val, max_val = INPUT_RANGES[field]
        if not (min_val <= value <= max_val):
            errors.append(f"'{field}' must be between {min_val} and {max_val}, got {value}")
    return errors

def predict_thalassemia(mother_age, father_age, mother_Hb, father_Hb, mother_MCV, father_MCV,
                        mother_HbA2, father_HbA2, mother_HbF, father_HbF, mother_MCH, father_MCH,
                        mother_RBC, father_RBC, mother_RDW, father_RDW):
    input_data = np.array([[mother_age, mother_Hb, mother_HbA2, mother_HbF, mother_MCV, mother_MCH,
                            mother_RBC, mother_RDW, father_age, father_Hb, father_HbA2, father_HbF,
                            father_MCV, father_MCH, father_RBC, father_RDW]])
    input_scaled = scaler.transform(input_data)
    prediction = model.predict(input_scaled)
    return label_encoder.inverse_transform(prediction)[0]

@app.route('/api/predict', methods=['POST', 'OPTIONS'])
def predict():
    if request.method == 'OPTIONS':
        # Handle preflight OPTIONS request
        return jsonify({"status": "OK"}), 200

    try:
        data = request.get_json()
        if not data or 'mother' not in data or 'father' not in data:
            return jsonify({"error": "Missing 'mother' or 'father' data"}), 400

        mother = data['mother']
        father = data['father']

        required_fields = ['age', 'hb', 'mcv', 'hba2', 'hbf', 'mch', 'rbc', 'rdw']
        for field in required_fields:
            if field not in mother or field not in father:
                return jsonify({"error": f"Missing field '{field}' in mother or father data"}), 400

        try:
            # Prepare inputs for validation
            inputs = {
                'mother_age': float(mother['age']),
                'father_age': float(father['age']),
                'mother_Hb': float(mother['hb']),
                'father_Hb': float(father['hb']),
                'mother_MCV': float(mother['mcv']),
                'father_MCV': float(father['mcv']),
                'mother_HbA2': float(mother['hba2']),
                'father_HbA2': float(father['hba2']),
                'mother_HbF': float(mother['hbf']),
                'father_HbF': float(father['hbf']),
                'mother_MCH': float(mother['mch']),
                'father_MCH': float(father['mch']),
                'mother_RBC': float(mother['rbc']),
                'father_RBC': float(father['rbc']),
                'mother_RDW': float(mother['rdw']),
                'father_RDW': float(father['rdw'])
            }
        except (ValueError, TypeError):
            return jsonify({"error": "Invalid numeric value in input data"}), 400

        # Validate input ranges
        validation_errors = validate_inputs(inputs)
        if validation_errors:
            return jsonify({"error": "Input validation failed", "details": validation_errors}), 400

        result = predict_thalassemia(
            inputs['mother_age'], inputs['father_age'], inputs['mother_Hb'], inputs['father_Hb'],
            inputs['mother_MCV'], inputs['father_MCV'], inputs['mother_HbA2'], inputs['father_HbA2'],
            inputs['mother_HbF'], inputs['father_HbF'], inputs['mother_MCH'], inputs['father_MCH'],
            inputs['mother_RBC'], inputs['father_RBC'], inputs['mother_RDW'], inputs['father_RDW']
        )
        return jsonify({"message": result})

    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)