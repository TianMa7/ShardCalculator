import requests
import json

API_KEY = "6a62a0c8-ee75-499f-8cb5-c464b6780439"#expires july 25 4pm

#fetch
response = requests.get("https://api.hypixel.net/v2/skyblock/bazaar?key=" + API_KEY)


ShardList = []


if response.status_code == 200:
    data = response.json()["products"]
    for item in data:
        if "SHARD_" in data[item]["quick_status"]["productId"]:
            ShardList.append(data[item]["quick_status"])

    #filtered_ShardList = [item for item in ShardList if "SHARD_" in item["productId"]]
    #print it pretty
    for item in ShardList:
        print("Name: "+ item["productId"] + "  " + "InstaBuy: " + str(item["sellPrice"]))
        # print(f"Name: {item['productId']}  InstaBuy: {item['sellPrice']}")
    print(len(ShardList))

    # with open("shardData.json", "w") as f:
    #     f.write(json.dumps(ShardList))
    #VERY IMPORTANT TO PROBABLY ONLY WRITE ONCE

    

else:
    print("tian is stupid and its his fault that the http request failed")