from flask import Flask, render_template, request, current_app as app
from flask_apscheduler import APScheduler
from sense_hat import SenseHat
import os
import requests
import datetime
import sqlite3
import sys



app = Flask(__name__)

@app.route('/')
def test():
    time = datetime.datetime.now()
    return render_template('main.html', time=time)



if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
