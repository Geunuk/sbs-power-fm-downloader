from urllib.request import urlopen
from bs4 import BeautifulSoup
from re import findall

def program_scrawl(url, station):

    sch_html = urlopen(url)
    sch_bs = BeautifulSoup(sch_html, "html.parser")

    pgm_info = []
    for program in sch_bs.find("tbody").findAll("tr"):

        pgm_name = program.td.a.get_text().strip()
        if findall("뉴스", pgm_name) != ["뉴스"]:
            pgm_time = program.th.div.get_text().strip()
            pgm_stion = station
            pgm_url = program.td.a.attrs["href"]
            down_url = to_down_url(pgm_url)
            pgm_info.append([pgm_name, pgm_time, pgm_stion, pgm_url, down_url])

    return pgm_info

def to_down_url(pgm_url):

    pgm_html = urlopen(pgm_url)
    pgm_bs = BeautifulSoup(pgm_html, "html.parser")
    print(pgm_bs)
    print(pgm_bs.find("frame", {"id" : "body"}))
    down_url = pgm_bs.find("frame", {"id" : "body"}).attrs["src"]
    down_url = findall("vVodId=V..........", down_url)
    down_url = "http://wizard2.sbs.co.kr/w3/template/tp1_podcast_radio_list_down.jsp?" + down_url[0]
	
    return down_url
