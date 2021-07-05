import json
import csv
import requests
from bs4 import BeautifulSoup


url = "https://bopis.mastermindtoys.com/ajax/getstorelocation.php"

headers = {
    "Referer": "https://www.mastermindtoys.com/",
}

payload = {
    "doAction": "getNearStoreData",
    "latitude": "",
    "longitude": "",
    "flagDisplayFirstRecord": "Y",
    "shopifyCustomerId": "",
    "selectedStoreInCookies": "",
}

data = requests.post(url, headers=headers, data=payload).json()


print(json.dumps(data, indent=4))

with open("test.csv", 'w', encoding="UTF-8", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=['id','name','address1','address2','city','postCode','province','phoneNumber','storeId'])
    writer.writeheader()
    for i, d in enumerate(data["details"], 1):
        writer.writerow({'id':i, 'name':d["name"], 'address1':d["address1"], 'address2':d["address2"], 'city':d["city"], 'postCode':d["postCode"], 'province':d["province"], 'phoneNumber':d["phoneNumber"], 'storeId':d["storeId"]})