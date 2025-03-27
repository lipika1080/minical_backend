from flask import Flask, request, jsonify
from flask_cors import CORS
from database import collection

app = Flask(__name__)
CORS(app)

@app.route("/calculate", methods=["POST"])
def calculate():
    data = request.json
    operation = data.get("operation")
    numbers = data.get("numbers")

    if not numbers or not isinstance(numbers, list):
        return jsonify({"error": "Invalid numbers format"}), 400

    if operation == "add":
        result = sum(numbers)
    elif operation == "subtract":
        result = numbers[0] - sum(numbers[1:])
    elif operation == "multiply":
        result = 1
        for num in numbers:
            result *= num
    elif operation == "divide":
        try:
            result = numbers[0]
            for num in numbers[1:]:
                result /= num
        except ZeroDivisionError:
            return jsonify({"error": "Cannot divide by zero"}), 400
    else:
        return jsonify({"error": "Invalid operation"}), 400

    # Save to Cosmos DB1
    record = {"operation": operation, "numbers": numbers, "result": result}
    collection.insert_one(record)

    return jsonify({"result": result})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
