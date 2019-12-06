from flask_mysqldb import MySQL
import MySQLdb.cursors

class UserDb():
	def __init__(self):
		self.key = os.urandom(24) #random number
		self.key = str(key)
		#secret_key generated
		self.app.secret_key = key
		#database connection
		self.app.config['MYSQL_HOST'] = 'localhost' #changes based on your installation
		self.app.config['MYSQL_USER'] = 'root'	   #changes based on your installation
		self.app.config['MYSQL_PASSWORD'] = '12345' #changes based on your installation
		self.app.config['MYSQL_DB'] = 'pythonlogin'   #changes based on your installation
		#mysql instance creaion
		self.mysql = MySQL(app)

	def get_account(self, username, password):
		cursor = self.mysql.connection.cursor(MySQLdb.cursors.DictCursor)
		cursor.execute('SELECT * FROM accounts WHERE username = %s AND password = %s',(username,password))
		return cursor.fetchone()