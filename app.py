from flask import Flask, render_template, request, redirect
import mysql.connector

app = Flask(__name__)

# Database connection
def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",               # Change if different
        password="10384",   # Change this to your MySQL password
        database="studentdb"
    )

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/add', methods=['GET', 'POST'])
def add_student():
    if request.method == 'POST':
        name = request.form['name']
        age = request.form['age']
        course = request.form['course']
        conn = get_connection()
        cur = conn.cursor()
        cur.execute("INSERT INTO student (name, age, course) VALUES (%s, %s, %s)", (name, age, course))
        conn.commit()
        conn.close()
        return redirect('/view')
    return render_template('add.html')

@app.route('/view')
def view_students():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM student")
    students = cur.fetchall()
    conn.close()
    return render_template('view.html', students=students)

@app.route('/update/<int:id>', methods=['GET', 'POST'])
def update_student(id):
    conn = get_connection()
    cur = conn.cursor()
    if request.method == 'POST':
        name = request.form['name']
        age = request.form['age']
        course = request.form['course']
        cur.execute("UPDATE student SET name=%s, age=%s, course=%s WHERE id=%s", (name, age, course, id))
        conn.commit()
        conn.close()
        return redirect('/view')
    else:
        cur.execute("SELECT * FROM student WHERE id=%s", (id,))
        student = cur.fetchone()
        conn.close()
        return render_template('update.html', student=student)

@app.route('/delete/<int:id>')
def delete_student(id):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("DELETE FROM student WHERE id=%s", (id,))
    conn.commit()
    conn.close()
    return redirect('/view')

if __name__ == '__main__':
    app.run(debug=True)
