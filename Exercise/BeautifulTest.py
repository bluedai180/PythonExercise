from bs4 import BeautifulSoup
import requests
from selenium import webdriver
import time
import sqlite3

driver = webdriver.PhantomJS()

ua = {  # 'User-Agent':'Mozilla/5.0 (compatible; Googlebot/2.1; +Googlebot - Webmaster Tools Help)',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2062.124 Safari/537.36',
    'Connection': 'Keep-Alive',
    'Accept-Language': 'zh-CN,zh;q=0.8',
    'Accept-Encoding': 'gzip,deflate,sdch',
    'Accept': '*/*',
    'Accept-Charset': 'GBK,utf-8;q=0.7,*;q=0.3',
    'Cache-Control': 'max-age=0'
}
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'
}


# driver.get(url)
#
# print(driver.page_source)
# soup = BeautifulSoup(driver.page_source, 'xml')
# print(soup.find_all('div')[4])


class PrivateVideo:
    i = 0
    title = ""
    pic = ""
    url_home = "http://sifangpian.xyz"
    url_index = "http://sifangpian.xyz/index/"

    def __init__(self):
        self.conn = sqlite3.connect('video.db')
        # self.cursor = self.conn.cursor()
        # self.conn.execute("DROP TABLE video")
        # self.cursor.execute('create table video (id INTEGER PRIMARY KEY NOT NULL, name TEXT, thumb TEXT, src TEXT)')

    def get_pages(self, index):
        # response_home = requests.get(self.url_index + "%s.html" % index, headers=headers, timeout=5)
        driver.get(self.url_index + "%s.html" % index)
        # soup_home = BeautifulSoup(response_home.text, "html5lib")
        soup_home = BeautifulSoup(driver.page_source, "html5lib")
        for link in soup_home.find_all("div", "thumb"):
            self.title = link.a.get("title")
            self.pic = link.img.get("data-original")
            try:
                self.get_item(self.url_home + link.a.get("href"))
            except AttributeError:
                print(self.title + "@@@@@@@@@@@AttributeError")
                continue

    def get_item(self, url_item):
        # response_item = requests.get(url_item, headers=headers)
        driver.get(url_item)
        # soup_item = BeautifulSoup(response_item.text, "html5lib")
        soup_item = BeautifulSoup(driver.page_source, "html5lib")
        self.get_video_link(soup_item.find(id="link3").get("value"))

    def get_video_link(self, url_video):
        # response_video = requests.get(url_video, headers=headers)
        driver.get(url_video)
        # soup1 = BeautifulSoup(response_video.text, "html5lib")
        soup1 = BeautifulSoup(driver.page_source, "html5lib")
        for link in soup1.find_all("source"):
            print(self.title)
            # print(self.pic)
            # print(link.get("src"))
            self.insert_db([str(self.title), str(self.pic), str(link.get("src"))])

    def insert_db(self, info):
        if self.conn.execute("SELECT * FROM video where name = '" + info[0] + "'").fetchone() is None:
            print("insert")
            self.conn.execute('insert into video (name, thumb, src) values (?, ?, ?)', info)

if __name__ == '__main__':
    pv = PrivateVideo()
    while pv.i < 1:
        pv.i += 1
        # time.sleep(5)
        pv.get_pages(str(pv.i))
    pv.conn.commit()
    pv.conn.close()
