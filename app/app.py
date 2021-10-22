import sys
from eventService import Events
from pubService import PubService
from subService import SubService

from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if request.form['submit_button'] == 'publisher':
            if request.form['pass'] == 'pppp':
                print('correct password!', file=sys.stderr)
                return redirect('/publishers')
            else:
                print('wrong password!', file=sys.stderr)
        elif request.form['submit_button'] == 'subscriber':
            if request.form['pass'] == 'ssss':
                print('correct password!', file=sys.stderr)
                return redirect('/subscribers')
            else:
                print('wrong password!', file=sys.stderr)
    return render_template('index.html')


@app.route('/publishers', methods=['GET', 'POST'])
def publishers():
    return render_template('pub.html')


@app.route('/subscribers', methods=['GET', 'POST'])
def subscribers():
    return render_template('sub.html')


if __name__ == '__main__':
    app.run(debug=True)
