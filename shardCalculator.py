#
def shardCalculator(shardList:dict, shard: dict, buyMethod: str, sellMethod: str) -> dict:
    #Dictionary of shard productID, buyPrice/sellPrice, buyPrice/sellPrice
    #shardlist is bazaar data
    id = shard["id"]
    prereq = shard["fusion_sources"]
    




    chamPrereqData = []
    basePrereqData = []
    chamData = []
    cheapestShards = [{
        "productId": "SHARD_MEGALITH",
        "sellPrice": float('inf'),
        "sellVolume": 422,
        "sellMovingWeek": 8259,
        "sellOrders": 27,
        "buyPrice": float('inf'),
        "buyVolume": 103389,
        "buyMovingWeek": 19782,
        "buyOrders": 956,
        "shardId": "L29"
    }for _ in range(5)]

    for item in prereq["base"]:
        for item2 in shardList:
            if item == item2["shardId"]:
                basePrereqData.append(item2)
                break

    for item in prereq["chameleon"]:
        for item2 in shardList:
            if item == item2["shardId"]:
                chamPrereqData.append(item2)
                break

    for item in shardList:
        if item["shardId"] == "L4":
            chamData.append(item)
            break  
        if item["shardId"][0] in ["C","U","R","E","L"] and item[buyMethod] < cheapestShards[0][buyMethod]:
            cheapestShards[0] = item
        if item["shardId"][0] in ["U","R","E","L"] and item[buyMethod] < cheapestShards[1][buyMethod]:
            cheapestShards[0] = item
        if item["shardId"][0] in ["R","E","L"] and item[buyMethod] < cheapestShards[2][buyMethod]:
            cheapestShards[0] = item
        if item["shardId"][0] in ["E","L"] and item[buyMethod] < cheapestShards[3][buyMethod]:
            cheapestShards[0] = item
        if item["shardId"][0] in ["L"] and item[buyMethod] < cheapestShards[4][buyMethod]:
            cheapestShards[0] = item
            



            






    


    


    #General function here:
    #Draws data out of a dictionary


    #1. Recieve input of what shard to check
    #2. Check prerequisites of fusion sources
    #3. Create a math function that outlines the cost of the fusion
    #3a. base + chameleon functions
    
    #IMPLIMENT THIS LATER
    #2a. check the possible special crafting recipies

    #2. Check and store shard price of everything on bazaar
    #3. input the bazaar prices into the calculator and compare outcomes to find cheapest method

    #4 OUTPUT: Dictionary of Cost, Return, Profit($$ amount with bazaar tax included), Profit(% amount with bazaar tax included)

    return {}



#can only be used if chameleon does not return as null
def chameleonCalc(prereqData: dict, buyMethod: str, sellMethod: str, chamData: dict) -> dict:
    returnOptions = []
    #chameleon only takes 2 to create
    for item in prereqData:
        price = (item["fusion_quantity"] * item[buyMethod]) + (2 * chamData[buyMethod])
        returnOptions.append({"price": price, "id1": item, "id2": chamData})
    
    if returnOptions:
        return min(returnOptions, key=lambda x: x["price"])
    else:
        return {}




#MUST TEST ISSUE: CAN I COMBINE A C9 and a C15 TO GET A C12?
#NOT DONE:
#must change all commented out lines
#find a way to get a list of data of cheapest shard of each category(fodder shards)

def baseCalc(prereqData: dict, buyMethod: str, sellMethod: str, cheapItem: dict) -> dict:
    #TODO: create a seperate function that creates dict cheapItem, which has a dictionary of the cheapest shard in each rarity





    returnOptions = []

    for item in prereqData:
        if item["shardId"][0] == "C":
            rarity = 0
        if item["shardId"][0] == "U":
            rarity = 1
        if item["shardId"][0] == "R":
            rarity = 2
        if item["shardId"][0] == "E":
            rarity = 3
        if item["shardId"][0] == "L":
            rarity = 4
        price = (item["fusion_quantity"] * item[buyMethod]) + (cheapItem[rarity]["fusion_quantity"] * cheapItem[rarity][buyMethod])
        returnOptions.append({"price": price, "id1": item, "id2": cheapItem[rarity]})
    
    #how do i make this return only the cheapest option
    if returnOptions:
        return min(returnOptions, key=lambda x: x["price"])
    else:
        return {}
        
        

