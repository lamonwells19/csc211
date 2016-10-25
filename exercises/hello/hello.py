#!/usr/bin/env python3

from flask import Flask,
app = Flask(__name__)
app.config{'TEMPLATES_AUTO_RELOAD'}=True
@app.route('/')
def hello_world():
    return "Hello World!"

@app.route('/test')
def test_function():
    return '<h1>Different more text</h>'

@app.route('/test/<int:number>')
def test_number(number):
    content = '<h1>Different more text for #{}</h1>'
    content = content.format(number)
    return content

@app.route('login',methods=['GET','POST'])
def login():
    if request.method =='POST':
        return "This is a POST"
    else
        return "This is a GET"

@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_templates('hello.html',)
