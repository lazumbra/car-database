import json

from bson import ObjectId
from flask import Flask, request
from pymongo import MongoClient

# Código reproduzido de um tutorial visto no youtube.


app = Flask(__name__)

client = MongoClient()
db = client.get_database('talk_pymongo')
collection = db.get_collection('cars')


@app.route('cars/create/', methods=['POST'])
def create():
    object_id = collection.insert(request.json)
    return


@app.route('cars/retrieve/', methods=['GET'])
def retrieve():
    filters = request.args.to_dict(flat=True)
    results = list(collection.find(filters))
    return json.dumps(
        results,
        default=lambda v: str(v) if isinstance(v, ObjectId) else v
    )


@app.route('/cars/update/<id>/', methods=['PATCH'])
def update(id):
    collection.update(
        {'_id': ObjectId(id)},
        {'$set': request.json}
    )
    return id


@app.route('/cars/delete/<id>/', methods=['DELETE'])
def delete(id):
    collection.remove({'_id': ObjectId(id)})
    return id
