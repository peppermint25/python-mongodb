from flask import Flask, render_template, request, jsonify
from bson.json_util import dumps
from bson.objectid import ObjectId
from pymongo import MongoClient

app = Flask(__name__)

client = MongoClient("mongodb+srv://mint:datubaze@cluster0.aiihewy.mongodb.net/?retryWrites=true&w=majority")
db = client.test
myCollection = db.test


@app.route("/")
def main():
    print("abc")
    #  cur = mysql.connection.cursor()
    #   cur.execute(db)
    # rv = cur.fetchall()
    #  print (rv)
    users = [{"id": 1, "name": "john"},
             {"id": 2, "name": "alise"}]
    return render_template('index.html', users=users)


@app.route("/show", methods=['GET'])
def show():
    names = db.test.find({}, "name")
    passwords = db.test.find({}, "password")

    return render_template('index.html', name=names, password=passwords)


@app.route("/add", methods=['GET','POST'])
def add():
    add = {}
    if request.method == 'POST':
        add['name'] = request.form['name']
        add['password'] = request.form['password']
        db.test.insert_one(add)
    return render_template('index.html')
    


@app.route("/delete/<id>", methods=['DELETE'])
def delete(id):
    client.db.test.delete_one({'_id': ObjectId(id)})
    resp = jsonify('User deleted successfully!')
    resp.status_code = 200
    return resp


if __name__ == "__main__":
    app.run(debug=True)