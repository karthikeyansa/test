import MySQLdb

class UserDb():
	def __init__(self):
		self.host = 'localhost'
		self.user = 'root'
		self.passwd = '12345'
		self.db = 'pythonlogin'
		self.conn = MySQLdb.connect(host= self.host, user = self.user, passwd = self.passwd, db = self.db)
		cur = self.conn.cursor()

	def get_account(self, username, password):
		cur = self.conn.cursor()
		cur.execute('SELECT * FROM accounts WHERE username = %s AND password = %s',(username,password))
		return(cur.fetchone())