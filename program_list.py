from find_program import *
from lib_tb import *

def mk_list(url, stion, cursor):

	pgm_info = program_scrawl(url, stion)
	insert_tb(cursor, pgm_info)

power_url = "http://w3.sbs.co.kr/schedule/scheduleSub.do?depth02=d2_3&depth03=power&channel=Power"
love_url = "http://w3.sbs.co.kr/schedule/scheduleSub.do?depth02=d2_3&depth03=love&channel=Love"

connection, cursor= connect_tb()
create_tb(cursor)
mk_list(power_url, "power", cursor)
mk_list(love_url, "love", cursor)

connection.commit()
print_tb(cursor)

connection.close()	
