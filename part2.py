from flask import Flask
from flask.ext.mysql import MySQL

# create module instance
app = Flask(__name__)
mysql = MySQL()

# MySQL configuration
app.config['MYSQL_DATABASE_USER'] = '*'
app.config['MYSQL_DATABASE_PASSWORD'] = '*'
app.config['MYSQL_DATABASE_DB'] = '*'
app.config['MYSQL_DATABASE_HOST'] = '*'
#app.config['MYSQL_DATABASE_PORT'] = '3306'
mysql.init_app(app)

# Create MySQL connection instance
conn = mysql.connect()

# Create a query cursor
cursor = conn.cursor()

# Routers
@app.route("/")
def main():
    return "Welcome!"

@app.route("/books")
def books():
    query = "SELECT * FROM book"
    cursor.execute(query)
    # query = SELECT * FROM %s"
    # param = ("book")
    # cursor.execute(query, param)
    data = cursor.fetchall()
    print(data)
    from flask import jsonify
    return jsonify(data)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)
