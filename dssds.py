import requests
from bs4 import BeautifulSoup
# response = requests.get("https://ua.sinoptik.ua/%D0%BF%D0%BE%D0%B3%D0%BE%D0%B4%D0%B0-%D0%BA%D0%B8%D1%97%D0%B2/2023-06-02")
#
# if response.status_code == 200:
#     soup = BeautifulSoup(response.text, features="html.parser")
#     soup_list = soup.find_all("td")
#     res = (soup_list[4], soup_list[20])
# b = res.text
# print(b)

response = requests.get("https://ua.sinoptik.ua/%D0%BF%D0%BE%D0%B3%D0%BE%D0%B4%D0%B0-%D0%BA%D0%B8%D1%97%D0%B2/2023-06-02")
if response.status_code == 200:
    soup = BeautifulSoup(response.text, features="html.parser")
    soup_list = soup.find_all("td")
    temperature = soup_list[20:27]
    time = soup_list[4:11]
a = (temperature[0].text, time[0].text)
print(a)

# print(temperature[0].text, time[0].text)

# from bs4 import BeautifulSoup
# import requests
# response = requests.get("https://ua.sinoptik.ua/%D0%BF%D0%BE%D0%B3%D0%BE%D0%B4%D0%B0-%D0%BA%D0%B8%D1%97%D0%B2/2023-06-01")
#
# if response.status_code == 200:
#     soup = BeautifulSoup(response.text, features="html.parser")
#     soup_list = soup.find_all("div", {"class":"main loaded"})
#     res = soup_list[0].find("p")
#     print(res)

# import requests
# res_parse_list = []
#
# response = requests.get("https://ua.sinoptik.ua/%D0%BF%D0%BE%D0%B3%D0%BE%D0%B4%D0%B0-%D0%BA%D0%B8%D1%97%D0%B2/2023-06-02")
# # print(response.text)
# response_text = response.text
# response_parse = response_text.split("td")
# for parse_elem_1 in response_parse:
#     if parse_elem_1.startswith("+"):
#         for parse_elem_2 in parse_elem_1.split("</td>"):
#             if parse_elem_2.startswith("+") and parse_elem_2[1].isdigit():
#                 res_parse_list.append(parse_elem_2)
#
# bitcoin_exchange_rate = res_parse_list[0]
# print(bitcoin_exchange_rate)