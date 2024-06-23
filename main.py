import os

from flask import Flask, jsonify, request
from flaskext.mysql import MySQL
from requets import requests

app = Flask(__name__)

mysql = MySQL()

app.config["MYSQL_DATABASE_USER"] = os.getenv("flasky_db_user")
app.config["MYSQL_DATABASE_PASSWORD"] = os.getenv("flasky_db_password")
app.config["MYSQL_DATABASE_DB"] = os.getenv("flasky_db_name")
app.config["MYSQL_DATABASE_HOST"] = "flasky-db"
app.config["MYSQL_DATABASE_PORT"] = 3306
mysql.init_app(app)

@app.route("/")
def landing():
    return jsonify({"API healthcheck": "OK"})

@app.route("/users", methods=["GET"])
def users():
    try:
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute("SELECT username, email FROM users")
        rows = cursor.fetchall()
        cursor.close()
        conn.close()
        resp = jsonify(rows)
        resp.status_code = 200
        return resp
    except Exception as exception:
        return jsonify(str(exception))

@app.route("/ipinfo/<ip_address>")
def data(ip_address):
    r = requests.get(f"https://ipinfo.io/{ip_address}")
    return jsonify(r.text)

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)