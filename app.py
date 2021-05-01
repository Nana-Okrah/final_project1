from flask import Flask, render_template, request, current_app as app
from flask_apscheduler import APScheduler
from sense_hat import SenseHat
import os
import requests
import datetime
import sqlite3
import sys

sense = SenseHat()

app = Flask(__name__)
scheduler = APScheduler()
scheduler.init_app(app)
scheduler.start()

@app.route('/task',)
def schedule_task():
    #scheduler.add_job(id=1, func=schedule_task, trigger='date', run_date=, args=[''])
    #time = datetime.datetime.now()
    
    return render_template('main.html')
@app.route('/all_task', methods=['GET', 'POST'])
def task():
    task=request.form['task']
    time=request.form['time']
    sense.show_message(task + "::" + time)
    return render_template('send.html',task=task, time=time )




if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
