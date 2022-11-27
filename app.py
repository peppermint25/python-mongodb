from bson.json_util import dumps
from bson.objectid import ObjectId
from flask import Flask, jsonify, render_template, request
from pymongo import MongoClient

app = Flask(__name__)
print ("abc")
#client = MongoClient("mongodb+srv://mint:datubaze@cluster0.aiihewy.mongodb.net/?retryWrites=true&w=majority")
client = MongoClient("mongodb://localhost:27017/")
client.db.A.insert_one({"name": "aa"})

db = client.test
print ("kakis")
print ("suns")
abc = client.db.A.find_one({})
print (abc)
#myCollection = db.test2


@app.route("/", methods=["GET"])
def main():
    #  cur = mysql.connection.cursor()
    #   cur.execute(db)
    # rv = cur.fetchall()
    #  print (rv)
    users = client.db.lietotaji.find({})
    users = list(users)
    print (users)
    return render_template('index.html', lietotaji=users)
    
@app.route("/add", methods=['POST'])
def add():
    print("aaaaaaaaaaaa", request.form)
    obj = {}
    obj['name'] = request.form['name']
    obj['password'] = request.form['password']
    lietotajs = client.db.lietotaji.insert_one(obj)
    ##return render_template('index.htmml')
    obj['_id'] = str(lietotajs.inserted_id)
    print ("add", obj)
    print ()
    
    return jsonify(**{"status": 200, "response": obj})


    


@app.route("/delete/<id>", methods=['DELETE'])
def delete(id):
    client.db.test.delete_one({'_id': ObjectId(id)})
    resp = jsonify('User deleted successfully!')
    resp.status_code = 200
    return resp

@app.route("/edit_profile/<id>", methods=["PUT"])
def update(id):
    print (id)
    edit = {
        "name": request.form['name'],
        "password": request.form['password'],
            }
    client.db.lietotaji.update_one({"_id" : ObjectId(id)},{ "$set": edit})
    return jsonify(**{"status": 200, "response": edit})


if __name__ == "__main__":
    app.run(debug=True)