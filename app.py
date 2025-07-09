from flask import Flask, render_template, request, redirect, url_for
import mysql.connector
from config import db_config

app = Flask(__name__)

# Database connection
def get_db_connection():
    return mysql.connector.connect(**db_config)

@app.route('/')
def index():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute('SELECT * FROM students')
    students = cursor.fetchall()
    conn.close()
    return render_template('index.html', students=students)

@app.route('/add', methods=['GET', 'POST'])
def add_student():
    if request.method == 'POST':
        name = request.form['name']
        age = request.form['age']
        email = request.form['email']
        
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('INSERT INTO students (name, age, email) VALUES (%s, %s, %s)', (name, age, email))
        conn.commit()
        conn.close()
        
        return redirect(url_for('index'))
    return render_template('add_student.html')

@app.route('/delete/<int:id>')
def delete_student(id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('DELETE FROM students WHERE id = %s', (id,))
    conn.commit()
    conn.close()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
