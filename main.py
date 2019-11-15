import webapp2
import MySQLdb
import passwords
import cgi
import cgitb

cgitb.enable()

class MainPage(webapp2.RequestHandler):
	def get(self):
		self.response.headers["Content-Type"] = "text/html"
		self.response.write("Hello world")

		conn = MySQLdb.connect(unix_socket = passwords.SQL_UNIX_SOCKET,
		user = passwords.SQL_USER,
		passwd = passwords.SQL_PASSWD,
		db = "kaz_database")
		cursor = conn.cursor()

		cursor.execute("SELECT * FROM kaz_table;")
		data = cursor.fetchall()
		self.response.write("<br><br>")
		self.response.write("  CPU: " + data[0][1])
#		self.response.write("  Company: " + data[0][2])
#		self.response.write("  Cores: " + data[0][3])
		cursor.close()
		conn.commit()
		conn.close()

app = webapp2.WSGIApplication ([("/", MainPage),], debug=True)
