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
    
    #time = datetime.datetime.now()
    
    return render_template('main.html')
@app.route('/all_task', methods=['GET', 'POST'])
def task():
    task=request.form['task']
    time=request.form['time']
    date=request.form['date']

    sense.show_message(task)
    conn = sqlite3.connect('./static/data/remind.db')
    curs = conn.cursor()
    curs.execute("INSERT INTO remind VALUES((?),(?),(?),(?))",(task, date, time))
    conn.commit()
    return render_template('main.html', task=task, time=time, date=date )
    
    
#@app.route()

    
@app.route('/task_edit', methods=['GET','POST'])
#scheduler.add_job(id=1, func=schedule_task, trigger='date', run_date=, args=[''])
def edit():
    
    return render_template('edit.html')
    
    
    return render_template('main.html',task=task)




if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
