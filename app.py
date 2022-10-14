from flask import Flask, render_template
import sys
import uuid as uuid
import sqlite3


app = Flask(__name__)




@app.route('/')
def index():
    return  render_template('index.html')
@app.route('/login')
def login():
    return  render_template('login.html')
@app.route('/home', methods=['POST'])
def home():
    return  render_template('index.html')

@app.route('/search')
def search():
    return  render_template('enhanced.html')

@app.route('/calendar')
def calendar():
    return  render_template('calendar.html')

@app.route('/jira')
def jira():
    return  render_template('jira.html')



if  __name__ == '__main__':
    app.run()