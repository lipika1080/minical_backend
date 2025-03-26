from flask import Flask, request, jsonify
from flask_cors import CORS
from pymongo import MongoClient
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
CORS(app)

# Connect to Azure Cosmos DB (Mongo API)
MONGO_URI = ("mongodb://minical:KjTwz5rMmFZ73MJUGaAop7K8KB9vVyriI4hF0voHGSEKKge8yTbmAmdZlgj875u0owf4wrJ1n0ejACDbylcW3A==@minical.mongo.cosmos.azure.com:10255/?ssl=true&replicaSet=globaldb&retrywrites=false&maxIdleTimeMS=120000&appName=@minical@")
client = MongoClient(MONGO_URI)
db = client["calculator_db"]
calculations = db["calculations"]

# Perform Addition
@app.route("/calculate/add", methods=["POST"])
def add_numbers():
    data = request.json
    result = sum(data["numbers"])
    calculations.insert_one({"operation": "add", "numbers": data["numbers"], "result": result})
    return jsonify({"operation": "addition", "result": result})

# Perform Subtraction
@app.route("/calculate/subtract", methods=["POST"])
def subtract_numbers():
    data = request.json
    result = data["numbers"][0] - sum(data["numbers"][1:])
    calculations.insert_one({"operation": "subtract", "numbers": data["numbers"], "result": result})
    return jsonify({"operation": "subtraction", "result": result})

# Perform Multiplication
@app.route("/calculate/multiply", methods=["POST"])
def multiply_numbers():
    data = request.json
    result = 1
    for num in data["numbers"]:
        result *= num
    calculations.insert_one({"operation": "multiply", "numbers": data["numbers"], "result": result})
    return jsonify({"operation": "multiplication", "result": result})

# Perform Division
@app.route("/calculate/divide", methods=["POST"])
def divide_numbers():
    data = request.json
    try:
        result = data["numbers"][0]
        for num in data["numbers"][1:]:
            result /= num
        calculations.insert_one({"operation": "divide", "numbers": data["numbers"], "result": result})
        return jsonify({"operation": "division", "result": result})
    except ZeroDivisionError:
        return jsonify({"error": "Cannot divide by zero"}), 400

if __name__ == "__main__":
    app.run(debug=True)
