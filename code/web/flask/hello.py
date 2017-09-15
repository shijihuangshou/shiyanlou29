# -*- coding:utf-8 -*-
from flask import Flask,session,escape,flash
from flask import render_template,request,redirect,url_for,abort
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)
@app.route('/upload',methods=['GET','POST'])
def upload():
	if request.method == 'GET':
		return render_template('upload.html')
	elif request.method == 'POST':
		f = request.files['file']
		fname = secure_filename(f.filename)
		f.save(os.path.join('./',fname))
		return '上传成功'
@app.route('/')
def hello_world():
	if 'username' in session:
		return render_template('hello.html',name=session['username'])
		#return 'Logged in as name %s' %escape(session['username'])
	return 'You are not logged in'
	#return redirect(url_for('upload'),302)
	
@app.route('/jerry')
def hello_jerry():
	return 'Hello jerry!'
@app.route('/sum/<int:a>/<int:b>/')
def add(a,b):
	sum = a+b
	return("%d+%d = %d"%(a,b,sum))
	
@app.route('/aaa')
def index():
	app.logger.error('An error occurred')
	abort(404)
	
	
@app.route('/login',methods=['GET','POST'])
def login():
	if request.method == 'POST':
		session['username'] = request.form['username']
		flash('You were successfully logged in')
		return redirect(url_for('hello_world'))
	elif request.method == 'GET':
		return render_template('login.html')
		
@app.route('/logout')
def logout():
	session.pop('username',None)
	return redirect(url_for('hello_world'))

@app.errorhandler(404)
def page_not_found(error):
	return render_template('page_not_found.html'), 404
	
if __name__ == '__main__':
	app.secret_key = 'this is a secret_key'
	app.run(debug=True)
	
	