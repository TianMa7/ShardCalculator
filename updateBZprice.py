import requests
import json

API_KEY = "01ad5a57-dbaf-47ec-b627-36325f2e167b" #expires jul 26 2:50pm Pacific

response = requests.get("https://api.hypixel.net/v2/skyblock/bazaar?key=" + API_KEY)



if response.status_code == 200:
    data = response.json()["products"]
    with open("shardDataFINALREAL1.json", 'r') as f:
        old_data = json.load(f)  
    
    dataToUpdate = ["sellPrice", "sellVolume", "sellMovingWeek", "sellOrders", "buyPrice", "buyVolume", "buyMovingWeek", "buyOrders"]

    for item in old_data:
        # update info
        new_quick_status = data[item]["quick_status"]
        for productData in dataToUpdate:
            old_data[item][productData] = new_quick_status[productData]

    with open("shardDataFINALREAL1.json", "w+") as f:
        json.dump(old_data, f)
        
else:
    print("tian is stupid and its his fault that the http request failed")