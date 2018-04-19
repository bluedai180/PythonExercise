import os

from bs4 import BeautifulSoup
import requests
import re
import sqlite3
import json


class Fitness:
    host = 'https://www.hiyd.com'

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'
    }

    def __init__(self):
        self.conn = sqlite3.connect('fitness_test.db')
        self.create_db()

    def get_pages(self, url):
        r = requests.get(url, headers=self.headers, timeout=5)
        soup = BeautifulSoup(r.text, "html.parser")
        for x in soup.find_all("div", class_="cont"):
            self.get_info(self.host + x.a.get('href'))
        next_page_url = str(soup.find("a", rel="next").get('href'))
        if next_page_url is not None and next_page_url != "/dongzuo/?page=3":
            self.get_pages(self.host + next_page_url)
        else:
            self.close_db()

    def get_info(self, url):
        r = requests.get(url, headers=self.headers, timeout=5)
        soup = BeautifulSoup(r.text, "html.parser")
        text = str(soup.find_all("script")[-1])
        data = json.loads(re.search(r'e.init\((.+?)\);', text).group(1))
        self.download(data['name'], data['video_url'])
        self.save_db([data['name'], data['muscle_name'], data['description'], data['video_url']])
        print("done " + data['name'])

    def download(self, name, url):
        if os.path.exists("./video") is False:
            os.makedirs("./video")
        with requests.get(url, stream=True) as response:
            with open("./video/" + name + ".mp4", "wb") as file:
                for data in response.iter_content(chunk_size=1024):
                    file.write(data)

    def create_db(self):
        self.conn.execute("CREATE TABLE IF NOT EXISTS fitness (id INTEGER PRIMARY KEY, "
                          "name TEXT, "
                          "muscle_name TEXT, "
                          "description TEXT, "
                          "video_url TEXT);")

    def save_db(self, data):
        self.conn.execute("INSERT INTO fitness (name, muscle_name, description, video_url) VALUES(?, ?, ?, ?)", data)

    def close_db(self):
        self.conn.commit()
        self.conn.close()


if __name__ == "__main__":
    fitness = Fitness()
    fitness.get_pages('https://www.hiyd.com/dongzuo/')











# import pymongo

# client = pymongo.MongoClient("localhost", 27017)
# db = client.fitness_database
# db_info = db.info

# conn = sqlite3.connect('fitness.db')

# conn.execute("CREATE TABLE fitness (id INTEGER PRIMARY KEY, "
#              "name TEXT, "
#              "difficulty_name TEXT, "
#              "trainingPoints TEXT, "
#              "category_name TEXT, "
#              "muscle TEXT, "
#              "muscle_id TEXT, "
#              "muscle_other_id TEXT, "
#              "equipments TEXT, "
#              "description TEXT, "
#              "video TEXT, "
#              "gif TEXT, "
#              "muscle_pic TEXT,"
#              "muscle_front_img TEXT, "
#              "muscle_back_img TEXT);")


# driver = webdriver.PhantomJS()


# class Fitness:
#     i = 0
#     url = "http://www.hiyd.com/dongzuo/"
#     headers = {
#         'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'
#     }
#
#
#     def get_info(self, url):
#         response = requests.get(url, headers=self.headers, timeout=5)
#         # driver.get(url)
#         soup = BeautifulSoup(response.text, "html.parser")
#         # soup = BeautifulSoup(driver.page_source, "html.parser")
#         text = str(soup.find_all("script")[-1])
#         # print(driver.page_source)
#         data_text = text.split("e.init(")[1].split(");")[0]
#         json_text = json.loads(data_text)
#         print(json_text)
#         other_muscle = json_text["otherMuscles"]
#         temp = []
#         if "name" not in json_text.keys():
#             return
#         if len(other_muscle) != 0:
#             for x in other_muscle:
#                 temp.append(self.change_muscle_id(x["muscle_id"]))
#         info = [json_text["name"],
#                 json_text["difficulty_name"],
#                 json_text["trainingPoints"],
#                 json_text["category_name"],
#                 json_text["muscle_name"],
#                 self.change_muscle_id(json_text["muscle_id"]),
#                 ",".join(temp),
#                 ("徒手训练" if json_text["equipments"][0] is None else json_text["equipments"][0]["name"]),
#                 json_text["description"],
#                 json_text["video_url"],
#                 json_text["gif"],
#                 json_text["muscle_pic"],
#                 json_text["muscle_front_img"],
#                 json_text["muscle_back_img"]]
#         print(info)
#         self.insert_db(info)
#
#     def insert_db(self, json_text):
#         conn.execute("INSERT INTO fitness (name, "
#                      "difficulty_name, "
#                      "trainingPoints, "
#                      "category_name, "
#                      "muscle, "
#                      "muscle_id, "
#                      "muscle_other_id, "
#                      "equipments, "
#                      "description, "
#                      "video, "
#                      "gif, "
#                      "muscle_pic, "
#                      "muscle_front_img, "
#                      "muscle_back_img) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", json_text)
#
#     def add_muscle_id(self):
#         sqlite_comm = "select * from fitness where category_name = %s;" % "'瑜伽'"
#         cursor = conn.execute(sqlite_comm)
#         for row in cursor:
#             print(row)
#
#     def change_muscle_id(self, muscle_id):
#         unknown = ["27", "28", "29", "30", "31", "32", "33", "34", "35", "36", "37"]
#         known = ["9", "21", "12", "19", "10", "16", "23", "20", "20", "16", "16"]
#         if muscle_id in unknown:
#             muscle_id = known[unknown.index(muscle_id)]
#         return muscle_id
#
#
# if __name__ == "__main__":
#     spider = Fitness()
#
#     while spider.i < 1602:
#         spider.i += 1
#         spider.get_info(spider.url + str(spider.i) + "/")
#         # try:
#         #     spider.get_info(spider.url + str(spider.i) + "/")
#         # except Exception:
#         #     print("Exception " + str(spider.i))
#         #     continue
#     conn.commit()
#     conn.close()
