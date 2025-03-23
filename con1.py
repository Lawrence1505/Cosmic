from flask import Flask, request, jsonify, render_template, redirect, url_for, session
from flask_mysqldb import MySQL
from flask_bcrypt import Bcrypt
from flask_jwt_extended import create_access_token, JWTManager
import os

app = Flask(__name__)
bcrypt = Bcrypt(app)

# Secret Key for Sessions & JWT
app.secret_key = os.urandom(24)
app.config['JWT_SECRET_KEY'] = 'your_jwt_secret'

# MySQL Config
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'yes@2871'
app.config['MYSQL_DB'] = 'your_database'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'

mysql = MySQL(app)
jwt = JWTManager(app)

# Render Login Page
@app.route('/')
def home():
    return render_template('index.html')

# Register User
@app.route('/register', methods=['POST'])
def register():
    data = request.json
    email = data.get('email')
    password = bcrypt.generate_password_hash(data.get('password')).decode('utf-8')

    cursor = mysql.connection.cursor()
    cursor.execute("INSERT INTO users (email, password) VALUES (%s, %s)", (email, password))
    mysql.connection.commit()
    cursor.close()
    
    return jsonify({"message": "User registered successfully"}), 201

# Login User
@app.route('/login', methods=['POST'])
def login():
    data = request.json
    email = data.get('email')
    password = data.get('password')

    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * FROM users WHERE email = %s", (email,))
    user = cursor.fetchone()
    cursor.close()

    if user and bcrypt.check_password_hash(user['password'], password):
        access_token = create_access_token(identity=user['id'])
        session['user_id'] = user['id']
        return jsonify({"message": "Login successful", "token": access_token}), 200
    else:
        return jsonify({"message": "Invalid credentials"}), 401

# Logout User
@app.route('/logout')
def logout():
    session.pop('user_id', None)
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)
