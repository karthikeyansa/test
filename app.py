from flask import Flask,request,redirect,url_for,render_template,session
from database import UserDb

app = Flask(__name__)
db = UserDb()

@app.route('/',methods=['GET','POST'])
def login():
	msg = ''
	if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
		username = request.form['username']
		password = request.form['password']
		account = db.get_account(username, password)
		#if account exists
		if account:
			#session creation
			session['loggedin'] = True
			session['id'] = account['id']
			session['username'] = account['username']
			#homepage
			return redirect(url_for('home'))
		else:
			#if account not found
			msg = 'invalid username and password!'
	return render_template('index.html',msg = msg)

if __name__ == '__main__':
	app.run(debug = True)
