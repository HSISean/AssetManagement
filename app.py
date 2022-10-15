from flask import Flask, render_template
import sys
import uuid as uuid
import sqlite3
import datetime


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

@app.route('/results')
def results():
    return  render_template('enhanced-results.html')

@app.route('/results/mac')
def mac_result():
    return  render_template('project-detail.html')


@app.route('/results/pc')
def pc_result():
    return  render_template('pc-details.html')

if  __name__ == '__main__':
    app.run()