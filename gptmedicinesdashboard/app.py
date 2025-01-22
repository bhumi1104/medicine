from flask import Flask, jsonify
from flask_cors import CORS
import random

app = Flask(__name__)
CORS(app)  # Allow cross-origin requests

# Mock Medicine Data
def generate_medicine_data():
    return {
        "inventory": {
            "total_medicines": 250,
            "out_of_stock": random.randint(0, 5),
            "near_expiry": random.randint(5, 15),
            "critical_stock_levels": random.randint(1, 5),
        },
        "usage": {
            "most_prescribed": [
                {"medicine": "Paracetamol", "prescriptions": random.randint(30, 100)},
                {"medicine": "Amoxicillin", "prescriptions": random.randint(20, 80)},
                {"medicine": "Ibuprofen", "prescriptions": random.randint(10, 60)},
            ],
            "medicine_usage_rate": [
                {"medicine": "Paracetamol", "usage_rate": random.uniform(2, 10)},
                {"medicine": "Amoxicillin", "usage_rate": random.uniform(1, 8)},
            ]
        },
        "financials": {
            "cost_of_medicines": round(random.uniform(2000, 5000), 2),
            "revenue_from_medicines": round(random.uniform(3000, 7000), 2),
            "stock_value": round(random.uniform(5000, 15000), 2),
        },
        "alerts": {
            "stock_out_alert": random.choice([True, False]),
            "expired_medicines_alert": random.choice([True, False]),
        }
    }

@app.route('/medicine_dashboard', methods=['GET'])
def get_medicine_dashboard_data():
    data = generate_medicine_data()
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
