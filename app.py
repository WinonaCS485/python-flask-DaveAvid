from flask import Flask, render_template
import pymysql
import pymysql.cursors

# Connect to the database
connection = pymysql.connect(host='mrbartucz.com',
                             user='rv7388ow',
                             password='S3qu3nc3112358',
                             db='rv7388ow_University',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)

try:
    with connection.cursor() as cursor:
        # Select from Students Table the name set as input
        sql = ("SELECT * from Student")

        # execute the SQL command
        cursor.execute(sql)
        output = cursor.fetchall()

finally: connection.close()

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/cakes')
def cakes():
    return 'Yummy cakes!'


@app.route('/database')
def database():
    return render_template('database.html', output=output)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=7388)
