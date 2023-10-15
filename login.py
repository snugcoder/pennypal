from flask import Flask, render_template, request, redirect, url_for, session
from flaskext.mysql import MySQL
from werkzeug.security import check_password_hash  # For password hashing

app = Flask(__name__)
app.secret_key = 'mysecretkey'

# Initialize the MySQL extension
mysql = MySQL(app)

#connect to database 
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'pythonlogin'
mysql = MySQL(app)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
         # Establish a database connection
        conn = mysql.connect()
        cursor = conn.cursor()

        # Add authentication logic here (e.g., check credentials against a database).
        # Execute an SQL query to retrieve the user's information
        cursor.execute("SELECT * FROM users WHERE username = %s", (username,))
        user = cursor.fetchone()

        if user is not None:
            # Compare the hashed password from the database with the provided password
            if check_password_hash(user[2], password):  # Assuming password is in the third column of the 'users' table
                session['username'] = user[0]  # Store the user's ID in the session
                return redirect(url_for('home'))
            else:
                error_message = 'Login failed. Please try again.'
    return render_template('login.html', error_message=error_message)


# to run the application
if __name__ == '__main__':
    app.run(debug=True)
