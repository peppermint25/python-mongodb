from bson.json_util import dumps
from bson.objectid import ObjectId
from flask import Flask, jsonify, render_template, request
from pymongo import MongoClient
from collections.abc import MutableMapping

app = Flask(__name__)
client = MongoClient("mongodb://db:27017/")
database = client.db
collection = database.leaderboard

@app.after_request
def after_request(response):
	response.headers.add('Access-Control-Allow-Origin', '*')
	response.headers.add('Access-Control-Allow-Headers', 'Content-Type')
	response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
	response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
	return response
    
@app.route('/add', methods=['POST'])
def add():
    obj = {}
    obj['username'] = request.json['username']
    obj['gametime'] = request.json['gametime']
    result = collection.insert_one(obj)
    return {'id': str(result.inserted_id)}

@app.route("/leaderboard-data", methods=["GET"])
def main():
    leaderboard = collection.find().sort([("gametime", 1)]).limit(10)
    leaderboard = list(leaderboard)
    leaderboard.sort(key=lambda x: float(x['gametime']))
    return dumps(leaderboard)
    # return jsonify(**{"status": 200, "response": leaderboard})

@app.route("/leaderboard-data/<entry_id>", methods=["DELETE"])
def delete_user(entry_id):
    result = collection.delete_one({"_id": ObjectId(entry_id)})
    if result.deleted_count > 0:
        return jsonify({"message": "User deleted from leaderboard"})
    else:
        return jsonify({"message": "User not found in leaderboard"})


if __name__ == "__main__":
    app.run(debug=False, host='0.0.0.0', port=5000, threaded=True)
