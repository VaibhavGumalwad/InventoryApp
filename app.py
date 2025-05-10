from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)
DB = 'inventory.db'

def init_db():
    with sqlite3.connect(DB) as conn:
        conn.execute('''
            CREATE TABLE IF NOT EXISTS inventory (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                quantity INTEGER NOT NULL
            )
        ''')

@app.route('/')
def index():
    with sqlite3.connect(DB) as conn:
        items = conn.execute('SELECT * FROM inventory').fetchall()
    return render_template('web.html', items=items)

@app.route('/add', methods=['POST'])
def add():
    name = request.form['name']
    quantity = int(request.form['quantity'])
    with sqlite3.connect(DB) as conn:
        conn.execute('INSERT INTO inventory (name, quantity) VALUES (?, ?)', (name, quantity))
    return redirect('/')

if __name__ == '__main__':
    init_db()
    app.run(host='0.0.0.0', port=5000)

