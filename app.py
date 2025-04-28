from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/api/v1.0/predict', methods=['GET'])
def predict():
    # Parametry
    a = request.args.get('a', default=0, type=float)
    b = request.args.get('b', default=0, type=float)
    
    # Reguła decyzyjna
    total = a + b
    prediction = 1 if total > 5.8 else 0

    # Odpowiedź
    response = {
        "prediction": prediction,
        "features": {"a": a, "b": b}
    }
    return jsonify(response)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
