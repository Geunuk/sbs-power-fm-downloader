from pymysql import connect, err, sys, cursors

def connect_tb():

	if True:

		host_name = input("input host : ")
		user_name = input("input user : ")
		pw_name = input("input password : ")
		db_name = input("input database : ")

	connection = connect(host=host_name, user=user_name, password=pw_name, db=db_name, charset='utf8')	
	cursor = connection.cursor(cursors.DictCursor);
	cursor.execute("set names utf8")
	if False:
		connection.close()
	return cursor

def create_tb(cursor):

	cursor.execute("CREATE TABLE IF NOT EXISTS schedule (id INTEGER NOT NULL AUTO_INCREMENT, name TEXT, time TEXT, station TEXT, pgm_url TEXT, down_url TEXT, primary key(id))")

def insert_tb(cursor, pgm_info):
	

	
	for val in pgm_info:	
		print(val[0], val[1], val[2], val[3], val[4])
		insert = 'INSERT INTO schedule (name, time, station, pgm_url, down_url) VALUES ("%s", "%s", "%s", "%s", "%s")' %(val[0], val[1], val[2], val[3], val[4])
		insert2 = "INSERT INTO schedule (name, time, station, pgm_url, down_url) VALUES ('abd', '2', '3', '4', '5')"
		cursor.execute(insert)
	
def print_tb(cursor):
	
	print = """SELECT name, time, station, pgm_url, down_url FROM schedule"""
