from pymysql import connect, cursors

def connect_tb():

	print("-" * 40)
	host_name = input("input host : ")
	user_name = input("input user : ")
	pw_name = input("input password : ")
	db_name = input("input database : ")

	connection = connect(host=host_name, user=user_name, password=pw_name,\
			     db=db_name, charset='utf8')	
	cursor = connection.cursor(cursors.DictCursor);
	cursor.execute("set names utf8")
	
	return connection, cursor

def create_tb(cursor):

	cursor.execute("CREATE TABLE IF NOT EXISTS schedule (id INTEGER NOT NULL AUTO_INCREMENT, name TEXT, time TEXT, station TEXT,\
			 pgm_url TEXT, down_url TEXT, primary key(id))")

def insert_tb(cursor, pgm_info):
		
	for part in pgm_info:

		insert = 'INSERT INTO schedule (name, time, station, pgm_url, down_url) VALUES\
			  ("%s", "%s", "%s", "%s", "%s")' %(part[0], part[1], part[2], part[3], part[4])
		cursor.execute(insert)
		
def print_tb(cursor):

	cursor.execute("SELECT name FROM schedule")	
	rows = cursor.fetchall()
	
	print("-" * 40)
	print("This Is the List of Program")
	print("-" * 40)
	for row in rows:
		print(row["name"])
	print("-" * 40)

	cursor.execute("SELECT name, down_url FROM schedule")
	rows = cursor.fetchall()
	return rows

def drop_tb(cursor):

	cursor.execute("DROP TABLE schedule")
	
	
