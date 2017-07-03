from datetime import date
from bs4 import BeautifulSoup
from urllib.request import urlopen, urlretrieve
import os
import re

def day_index(day):
	
	result = []

	day_list = day.split(" ")
	for day in day_list:

		if day == 'mon':

			result.append(0)
		
		elif day == 'tue':

			result.append(1)

		elif day == 'wed':

			result.append(2)
		elif day == 'thu':

			result.append(3)

		elif day == 'fri':

			result.append(4)

		elif day == 'sat':

			result.append(5)
		
		elif day == 'sun':
			result.append(6)
	
	return result


def date_format(date_str):
	
	date_list = date_str.split('-')
	
	return date(int(date_list[0]), int(date_list[1]), int(date_list[2]))


def url_change(down_url):
	
	old = re.findall("page=\d", down_url)
	if old == []:

		down_url = down_url + "&cpage=2"

	else:
		old_page = old[0]
		new_page = old_page[:5] + str(int(old_page[5:]) + 1)
		down_url = re.sub(old_page, new_page, down_url)
	
	return down_url



def down_pgm(pgm_name, down_url):

	if False:
		print("Input Period Want to Download")
		start = input("Start : ")
		end = input("End : ")
		print("-" * 40)

		print("Input Day of the Week Want to Download")
		day = input("Day : ")

	start = "2017-05-01"
	end = "2017-05-015"
	day = "mon"

	day_list = day_index(day)
	start = date_format(start)
	end = date_format(end)

	down_html = urlopen(down_url)
	down_bs = BeautifulSoup(down_html, "html.parser")

	episodes = down_bs.find("tbody").findAll("tr")
	for i in range(0, len(episodes)):
		
		episode = episodes[i].findAll("td")

		epi_name = episode[1].get_text()
		epi_date = episode[0].get_text()
		epi_date = epi_date.replace('.', '-')
		epi_date = date_format(epi_date)
		
		if epi_date < start:
			
			print("-" * 40)
			print("This is the End")
			print("-" * 40)
			return 0

		day_check = epi_date.weekday() in day_list
		period_check = start <= epi_date <= end
		
		if day_check == True and period_check == True:
			
			epi_name = epi_date.isoformat() + epi_name
			print("Downloading " + "\""  + epi_name + "\"")
			directory = "/media/geunukj/DATA/sbs_radio_downloader/%s" % pgm_name
		
			if not os.path.exists(directory):
				os.mkdir(directory)
			
			urlretrieve(episode[2].input.attrs["value"], directory + "/" + epi_name + ".mp3")
	
	next_page = url_change(down_url)
	down_pgm(pgm_name, next_page)
