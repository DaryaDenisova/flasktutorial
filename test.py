from flask import Flask
from flask import render_template
from flask import request
import db
import sqlite3
app = Flask(__name__)




@app.route('/')
def hello_world():
    # Connecting to DB
    conn = sqlite3.connect('app.db')
    c = conn.cursor()

    # Handler logic here
    c.execute("SELECT * FROM users")
    users = list(c.fetchall())

    # Close connection
    conn.close()
    # Return resulting HTML
    return render_template('page01.html', users=users)


@app.route('/search')
def search_for_person():
    q = request.args.get('query')
    users = db.get_users_by_name(q)
    return render_template('search_results.html', q=q, users=users)




app.run()
