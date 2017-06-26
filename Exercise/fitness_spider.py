from bs4 import BeautifulSoup
import requests
from selenium import webdriver
import time
import sqlite3
from selenium import webdriver
import json
import pymongo

# client = pymongo.MongoClient("localhost", 27017)
# db = client.fitness_database
# db_info = db.info

conn = sqlite3.connect('fitness.db')


conn.execute("CREATE TABLE fitness (id INTEGER PRIMARY KEY, "
             "name TEXT, "
             "difficulty_name TEXT, "
             "trainingPoints TEXT, "
             "category_name TEXT, "
             "equipments TEXT, "
             "description TEXT, "
             "video TEXT, "
             "gif TEXT, "
             "muscle_pic TEXT,"
             "muscle_front_img TEXT, "
             "muscle_back_img TEXT);")

# driver = webdriver.PhantomJS()


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
        info = [json_text["name"],
                json_text["difficulty_name"],
                json_text["trainingPoints"],
                json_text["category_name"],
                ("徒手训练" if json_text["equipments"][0] is None else json_text["equipments"][0]["name"]),
                json_text["description"],
                json_text["video_url"],
                json_text["gif"],
                json_text["muscle_pic"],
                json_text["muscle_front_img"],
                json_text["muscle_back_img"]]
        self.insert_db(info)

    def insert_db(self, json_text):
        conn.execute("INSERT INTO fitness (name, "
                     "difficulty_name, "
                     "trainingPoints, "
                     "category_name, "
                     "equipments, "
                     "description, "
                     "video, "
                     "gif, "
                     "muscle_pic, "
                     "muscle_front_img, "
                     "muscle_back_img) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", json_text)


if __name__ == "__main__":
    spider = Fitness()
    while spider.i < 1602:
        spider.i += 1
        spider.get_info(spider.url + str(spider.i) + "/")
        # try:
        #     spider.get_info(spider.url + str(spider.i) + "/")
        # except Exception:
        #     print("Exception " + str(spider.i))
        #     continue
    conn.commit()
    conn.close()
