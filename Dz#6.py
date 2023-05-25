# import requests
# from bs4 import BeautifulSoup
# response = requests.get("https://www.oschadbank.ua/currency-rate")
#
# if response.status_code == 200:
#     soup = BeautifulSoup(response.text, features="html.parser")
#     soup_list = soup.find_all("td",{"class":"heading-block-currency-rate__table-col"})
#     res = soup_list[10]
# b = float(res.text)
# print(b)


print(f"1. Usd"
      "\n2. Euro"
      "\n3. Japanese_yen"
      "\n4. Pounds")
r = int(input("Enter the number under which the currency you need is located: "))
a = int(input("Enter the amount(in UAH): "))
usd = 36.93
euro = 40.25
japanese_yen = 0.251
pounds = 45.59
converted = "Converted"

if r == 1:
    print(f"{converted:-^65}")
    print(a/usd)
elif r == 2:
    print(f"{converted:-^65}")
    print(a/euro)
elif r == 3:
    print(f"{converted:-^65}")
    print(a/japanese_yen)
elif r == 4:
    print(f"{converted:-^65}")
    print(a/pounds)
else:
    print(f"We do not have a currency number {r}, enter the one that is available.")
