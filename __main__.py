from find_program import *
from lib_tb import *
from down_pgm import down_pgm, input_cond

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
pgm_info = print_tb(cursor)
drop_tb(cursor)
connection.close()	

pgm_name, down_url, start, end, day_list = input_cond(pgm_info)
down_pgm(pgm_name, down_url, start, end, day_list)

