from flask import Flask
from flask.ext.mysql import MySQL

# create module instance
app = Flask(__name__)
mysql = MySQL()

# MySQL configuration
app.config['MYSQL_DATABASE_USER'] = ''
app.config['MYSQL_DATABASE_PASSWORD'] = ''
app.config['MYSQL_DATABASE_DB'] = ''
app.config['MYSQL_DATABASE_HOST'] = ''
mysql.init_app(app)

# Create MySQL connection instance
conn = mysql.connect()

# Create a query cursor
cursor = conn.cursor()

# Routers
@app.route("/")
def main():
    return "Welcome!"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)
