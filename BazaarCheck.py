import requests

API_KEY = "6a62a0c8-ee75-499f-8cb5-c464b6780439"#expires july 25 4pm

#fetch
response = requests.get("https://api.hypixel.net/v2/skyblock/bazaar?key=" + API_KEY)

if response.status_code == 200:
    data = response.json()
    # print(response.json())
    product = data["products"]["INK_SACK:3"]["quick_status"]
    # quick_status = product["quick_status"]

    print(product)
else:
    print("tian is stupid and its his fault that the http request failed")