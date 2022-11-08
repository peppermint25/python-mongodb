from flask import Flask, render_template, request, jsonify
from pymongo import MongoClient

app = Flask(__name__)

client = MongoClient("mongodb+srv://mint:<datubaze>@cluster0.aiihewy.mongodb.net/?retryWrites=true&w=majority", server_api=ServerApi('1'))
db = client.test
myCollection = db.test



@app.route("/")
def main():
    print ("abc")
  #  cur = mysql.connection.cursor()
 #   cur.execute("""SELECT user, host FROM mysql.user""")
   # rv = cur.fetchall()
  #  print (rv)
    users=[{"id": 1, "name": "john" },
           {"id": 2, "name": "alise" }]
    return render_template('index.html',  users=users)

@app.route("/show", methods=['GET'])
def bbox():
    print ("123")
    return jsonify(**{"status": 111,})


if __name__ == "__main__":
    app.run()