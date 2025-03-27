from pymongo import MongoClient

COSMOS_CONNECTION_STRING = "mongodb://minical:KjTwz5rMmFZ73MJUGaAop7K8KB9vVyriI4hF0voHGSEKKge8yTbmAmdZlgj875u0owf4wrJ1n0ejACDbylcW3A==@minical.mongo.cosmos.azure.com:10255/?ssl=true&replicaSet=globaldb&retrywrites=false&maxIdleTimeMS=120000&appName=@minical@"
client = MongoClient(COSMOS_CONNECTION_STRING)
db = client["calculatorDB"]
collection = db["calculations"]
