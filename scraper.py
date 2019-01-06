import datetime

from selenium import webdriver
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoAlertPresentException, WebDriverException, TimeoutException, NoSuchElementException
from bs4 import BeautifulSoup

from episode import Episode

sbs_url = "https://www.sbs.co.kr/"
return_html_string = "return document.documentElement.outerHTML"
download_url_prefix = "https://programs.sbs.co.kr"


class NoBannerException(Exception):
    def __str__(self):
        return "No banner at the page"


class NoDownBannerException(Exception):
    def __str__(self):
        return "No download banner at the page"


def get_programs(driver):
    driver.get(sbs_url)
    driver.find_element_by_id("sbs-gnb-header-program-button-open").click()

    allprog = driver.find_element_by_class_name("allprog_inner_powerfm")
    next_btn = allprog.find_element_by_class_name("program_btn_next")
    next_btn_enabled = True

    program_dict = {}
    while next_btn_enabled:
        if "disable" in next_btn.get_attribute("class") != None:
            next_btn_enabled = False
        else:
            next_btn_enabled = True

        sbs_html = driver.execute_script(return_html_string)
        sbs_soup = BeautifulSoup(sbs_html, "html.parser")
        powerfm = sbs_soup.find("div", class_="allprog_inner_powerfm")
        programs = powerfm.find_all("a", class_="ap_link")
        for program in programs:
            print(program.text, program["href"])
            program_dict[program.text] = program["href"]

        next_btn.click()
        allprog = driver.find_element_by_class_name("allprog_inner_powerfm")
        next_btn = allprog.find_element_by_class_name("program_btn_next")

    return program_dict

def get_episodes(driver, program_down_url):
    driver.get(program_down_url)
    try:
        element_present = EC.presence_of_element_located((By.CLASS_NAME, "podcast_list_inner"))
        WebDriverWait(driver, 20).until(element_present)
    except TimeoutException:
        print("timed out waiting for page to load")

    page = 1
    result = []
    while True:
        print("Download page {}".format(page))
        program_down_html = driver.execute_script(return_html_string)
        program_down_soup = BeautifulSoup(program_down_html, "html.parser")
        episodes = program_down_soup.find_all("li", class_="podcast_list_inner")

        for i, episode in enumerate(episodes):
            date = episode.select("span")[0].text.strip()
            date = datetime.datetime.strptime(date, "%Y.%m.%d")
            name = episode.select("strong")[0].text.strip()
            url = episode.select("div > a")[0]["href"].strip()
            url = download_url_prefix + url

            e = Episode(date, name, url)
            result.append(e)
            print(e)

            if i == 0:
                first_date = date.strftime("%Y%m%d")
        return result
        try:
            next_download_page(driver, page, first_date)
            page += 1
        except NoSuchElementException:
            return result

def get_episodes_cond(driver, program_down_url, start_date, end_date, week_days):
    driver.get(program_down_url)
    try:
        element_present = EC.presence_of_element_located((By.CLASS_NAME, "podcast_list_inner"))
        WebDriverWait(driver, 20).until(element_present)
    except TimeoutException:
        print("timed out waiting for page to load")

    page = 1
    result = []
    while True:
        print("Download page {}".format(page))
        program_down_html = driver.execute_script(return_html_string)
        program_down_soup = BeautifulSoup(program_down_html, "html.parser")
        episodes = program_down_soup.find_all("li", class_="podcast_list_inner")

        for i, episode in enumerate(episodes):
            date = episode.select("span")[0].text.strip()
            date = datetime.datetime.strptime(date, "%Y.%m.%d")
            name = episode.select("strong")[0].text.strip()
            url = episode.select("div > a")[0]["href"].strip()
            url = download_url_prefix + url

            if i == 0:
                first_date = date.strftime("%Y%m%d")

            if date < start_date:
                return result
            elif date <= end_date and date.weekday() in week_days:
                e = Episode(date, name, url)
                result.append(e)
                print(e)

        try:
            next_download_page(driver, page, first_date)
            page += 1
        except NoSuchElementException:
            return result


def next_download_page(driver, page, first_date):
    def not_text_topresent_in_element(_driver):
        element_present = EC.text_to_be_present_in_element((By.CLASS_NAME, "podcast_date"), first_date)
        return not element_present(_driver)

    id_ = "program-front-radio-pagination-"
    if page % 10 == 0:
        id_ += "next"
    else:
        next_page = page + 1
        id_ += "page-" + str(next_page)

    driver.find_element_by_id(id_).click()
    try:
        WebDriverWait(driver, 20).until(not_text_topresent_in_element)
    except TimeoutException:
        print("timed out waiting for page to load")

def check_down_link(program_soup):
    program_down_url = program_soup.find("div", {"id": "program-front-main-replay"})
    program_down_url = program_down_url.find("h3")
    program_down_url = program_down_url.select("a")[0]["href"]
    return program_down_url


def check_middle_link(program_soup):
    banner = program_soup.find("div", class_="bnr_inner slick-slide slick-current slick-active")
    if banner == None:
        raise NoBannerException
    if "다시듣기" in banner.select("a > span > img")[0]["alt"]:
        return program_soup.find("div", class_="bnr_inner slick-slide slick-current slick-active").select("a")[0][
            "href"]
    else:
        raise NoDownBannerException


def check_top_link(program_soup):
    items = program_soup.find("div", class_="program_lnb_w").find_all("li")
    for item in items:
        if "다시듣기" in item.select("a")[0].text:
            program_down_url = item.select("a")[0]["href"]
            return program_down_url


def get_download_url(driver, program_url):
    driver.get(program_url)
    try:
        element_present = EC.presence_of_element_located((By.CLASS_NAME, "pm_title_radio"))
        WebDriverWait(driver, 20).until(element_present)
    except TimeoutException:
        print("timed out waiting for page to load")

    program_html = driver.execute_script("return document.documentElement.outerHTML")
    program_soup = BeautifulSoup(program_html, "html.parser")
    for fun in [check_down_link, check_middle_link, check_top_link]:
        try:
            program_down_url = fun(program_soup)
        except AttributeError:
            continue
        except IndexError:
            continue
        except WebDriverException:
            continue
        except NoBannerException:
            continue
        except NoDownBannerException:
            continue

        try:
            driver.get(program_down_url)
            Alert(driver).dismiss()
        except NoAlertPresentException:
            return program_down_url
        except:
            print("[Fail] Cannot get download url from {}".format(program_url))
            return None
        else:
            continue
    else:
        return None

def total_test():
    driver = webdriver.Chrome()
    program_dict = get_programs(driver)
    for program_name, program_url in program_dict.items():
        program_down_url = get_download_url(driver, program_url)
        if program_down_url != None:
            print("[SUCCESS]", program_name, program_down_url)
            get_episodes(driver, program_down_url)
        else:
            print("[FAIL]", program_name, program_down_url)

def download_test():
    program_url = "https://programs.sbs.co.kr/radio/ten"#sominyoungstreet"
    driver = webdriver.Chrome()
    program_down_url = get_download_url(driver, program_url)
    get_episodes(driver, program_down_url)

def download_cond_test():
    import datetime

    program_url = "https://programs.sbs.co.kr/radio/ten"#sominyoungstreet"
    driver = webdriver.Chrome()
    program_down_url = get_download_url(driver, program_url)

    now = datetime.datetime.now()
    sevenago = now - datetime.timedelta(days=14)
    week_days = [1, 3, 4]
    get_episodes_cond(driver, program_down_url, sevenago, now,week_days)


def main():
    #total_text()
    #download_test()
    download_cond_test()

if __name__ == '__main__':
    main()
