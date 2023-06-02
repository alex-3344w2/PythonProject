import sqlite3
import requests
from bs4 import BeautifulSoup

connection = sqlite3.connect("itstep_DB1.sl3", 5)
cur = connection.cursor()
response = requests.get("https://ua.sinoptik.ua/%D0%BF%D0%BE%D0%B3%D0%BE%D0%B4%D0%B0-%D0%BA%D0%B8%D1%97%D0%B2/2023-06-02")
if response.status_code == 200:
    soup = BeautifulSoup(response.text, features="html.parser")
    soup_list = soup.find_all("td")
    temperature = soup_list[20:28]
    time = soup_list[4:12]
ab = "02 Червня"
a = (time[0].text, temperature[0].text)
b = (time[1].text, temperature[1].text)
c = (time[2].text, temperature[2].text)
d = (time[3].text, temperature[3].text)
e = (time[4].text, temperature[4].text)
f = (time[5].text, temperature[5].text)
g = (time[6].text, temperature[6].text)
j = (time[7].text, temperature[7].text)



# cur.execute("CREATE TABLE weather (time TEXT, temperature TEXT);")
cur.execute("INSERT INTO weather (time) VALUES ('02 Червня');")
cur.execute("INSERT INTO weather (time, temperature) VALUES (?,?);", a)
cur.execute("INSERT INTO weather (time, temperature) VALUES (?,?);", b)
cur.execute("INSERT INTO weather (time, temperature) VALUES (?,?);", c)
cur.execute("INSERT INTO weather (time, temperature) VALUES (?,?);", d)
cur.execute("INSERT INTO weather (time, temperature) VALUES (?,?);", e)
cur.execute("INSERT INTO weather (time, temperature) VALUES (?,?);", f)
cur.execute("INSERT INTO weather (time, temperature) VALUES (?,?);", g)
cur.execute("INSERT INTO weather (time, temperature) VALUES (?,?);", j)

connection.commit()
connection.close()

