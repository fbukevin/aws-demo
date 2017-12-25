
## Part I - Create Web Server
1. create an AWS accout (no credit card required for register)
2. create an EC2 instance with **Amazon Linux AMI**
    * Note
    1. Security Group should allow ssh, http, https accessibility
    2. Remeber download your PEM key and change its mode to 400 (`chmod 400 xxx.pem`)
3. connect to instance via `ssh -i .ssh/your_key.pem ec2-user@<domain_name>`)
4. install flask: `sudo pip install flask`
5. vim part1.py

```py
from flask import Flask

app = Flask(__name__)

@app.route("/")
def main():
    return "Welcome!"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)
```

6. run `sudo python part1.py`
7. go to your web browser and connect to `<domain_name>` to see if the web server shows `Welcome!` to you


## Part II - Connect to Database

1. Create RDS instance
    * remember to allow port 3306 for accessing in Security Group of RDS
2. sudo yum install -y mysql
3. create table
    1. connect to RDS instance: `mysql –u nccu –p –h <endpoint>`
        * use the "Master username" and "Master password" 
    2. select database `use nccu_demo`
    3. create table
    ```sql
    CREATE TABLE book (
        `book_id` int(11) NOT NULL auto_increment,
        `book_name` char(35) NOT NULL default '',
        `author` char(35) NOT NULL default '',
        PRIMARY KEY (`book_id`)
    );
    ```
    4. insert data
    ```sql
    insert into book (book_name, author) values ('Introduction to AWS', 'veck');
    ```
    5. query
	```sql
    select * from book;
    ```
4. sudo pip install flask-mysql
5. vim app.py
    * insert MySQL connection snippet
    ```python
    from flask.ext.mysql import MySQL

    # create module instance
    app = Flask(__name__)
    mysql = MySQL()

    # MySQL configuration
    app.config['MYSQL_DATABASE_USER'] = '*'
    app.config['MYSQL_DATABASE_PASSWORD'] = '*'
    app.config['MYSQL_DATABASE_DB'] = '*'
    app.config['MYSQL_DATABASE_HOST'] = '*'
    mysql.init_app(app)

    # Create MySQL connection instance
    conn = mysql.connect()

    # Create a query cursor
    cursor = conn.cursor()
    ```
    * create a new router and query with cursor
    ```python
    @app.route("/books")
    def books():
        query = "SELECT * FROM book"
        cursor.execute(query)
        data = cursor.fetchall()
        print(data)
        from flask import jsonify
        return jsonify(data)
    ```
6. run `sudo python part2.py`
7. go to your web browser and connect to `<domain_name>` to see if the web server shows data to you