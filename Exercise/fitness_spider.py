from bs4 import BeautifulSoup
import requests
from selenium import webdriver
import time
import sqlite3
from selenium import webdriver
import json

driver = webdriver.PhantomJS()
class Fitness:
    i = 0
    url = "http://www.hiyd.com/dongzuo/"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'
    }
    def get_info(self, url):
        response = requests.get(url, headers=self.headers, timeout=5)
        # driver.get(url)
        soup = BeautifulSoup(response.text, "html.parser")
        # soup = BeautifulSoup(driver.page_source, "html.parser")
        text = str(soup.find_all("script")[-1])
        # print(driver.page_source)
        data_text = text.split("e.init(")[1].split(");")[0]
        json_text = json.loads(data_text)
        print(json_text)

if __name__ == "__main__":
    spider = Fitness()
    while spider.i < 1:
        spider.i += 1
        spider.get_info(spider.url + str(spider.i) + "/")