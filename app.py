from flask import Flask, render_template, request, redirect
import mysql.connector

app = Flask(__name__)

def get_db_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",          # default XAMPP MySQL user
        password="",          # default has no password
        database="hotel_db"
    )

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/booking')
def booking():
    return render_template('booking.html')

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    email = request.form['email']
    checkin = request.form['checkin']
    checkout = request.form['checkout']
    room_type = request.form['room_type']

    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO bookings (name, email, checkin, checkout, room_type) VALUES (%s, %s, %s, %s, %s)",
        (name, email, checkin, checkout, room_type)
    )
    conn.commit()
    cursor.close()
    conn.close()

    return redirect('/bookings')

@app.route('/bookings')
def bookings():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM bookings")
    rows = cursor.fetchall()
    cursor.close()
    conn.close()
    return render_template('bookings.html', bookings=rows)

if __name__ == '__main__':
    app.run(debug=True)