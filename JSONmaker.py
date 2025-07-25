#A python program to assign shard id's to items
import json


print("Welcome to Tian's awesome and very useful json editor!")
print("Please enter what json file to access(PUT IN THIS).json: ")
fileName = input() + ".json"
#^This figures out what JSON file to access

print("Doing magic stuff...")
try:
    with open(fileName, "r") as f:
        data = json.load(f)
except FileNotFoundError:
    print("File not found, try again")
except json.JSONDecodeError as e:
    print(f"Error decoding JSON: {e}")
print("Loading complete")
#Loads json into a dictionary

print("What action would you like to take?")
print("1. add shard ID to shard Data")
userInput = str(input())
#menu page

if userInput == "1":
    print("1. add shard ID to shard Data ---> is selected")
    for item in data:
        print(item["productId"] + " is selected. type EXIT to leave or input the shard ID")
        userInput = str(input()).strip().upper()
        if userInput == "EXIT":
            print("have a good one")
            break
        else:
            item.update({"shardId":userInput})
            print(item["productId"] + " " + item["shardId"])
#option 1
    



print("now that are you done, would you like to save the file?(YES or NO)")
userInput = input().upper()
if userInput == "NO":
    print("ok idk what you were thinking, have a nice day!")
else:#on purpose in case something is mistyped
    print("What file name do you want to save this as?")
    userInput = input()
    with open(userInput+".json", "w") as JSON_file:
        json.dump(data, JSON_file)
    print("finished writing file. Have a nice day!")
#saves file