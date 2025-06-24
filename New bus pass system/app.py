from flask import Flask, render_template, request, redirect, url_for
import sqlite3
from datetime import datetime

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('bus_pass.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def home():
    return render_template('login.html')

@app.route('/apply', methods=['GET', 'POST'])
def apply_pass():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        route = request.form['route']
        conn = get_db_connection()
        conn.execute("INSERT INTO bus_passes (name, email, route, date_applied, status) VALUES (?, ?, ?, ?, ?)",
                     (name, email, route, datetime.now().date(), 'Pending'))
        conn.commit()
        conn.close()
        return 'Application Submitted Successfully!'
    return render_template('apply_pass.html')

@app.route('/admin', methods=['GET', 'POST'])
def admin_dashboard():
    conn = get_db_connection()
    if request.method == 'POST':
        pass_id = request.form['pass_id']
        status = request.form['status']
        conn.execute("UPDATE bus_passes SET status = ? WHERE id = ?", (status, pass_id))
        conn.commit()
    passes = conn.execute("SELECT * FROM bus_passes").fetchall()
    conn.close()
    return render_template('admin_dashboard.html', passes=passes)

if __name__ == '__main__':
    app.run(debug=True)