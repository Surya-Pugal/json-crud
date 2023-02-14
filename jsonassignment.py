import sys
import json

# print(str(sys.argv))
# dic={"name" : sys.argv[1], "city" : sys.argv[2]}
# print(dict)

# def updatejson():
#     # read method
#     f = open("jsoncrud.json")
#     data=json.load(f)
#     print(data)
#     f = open("jsoncrud.json", "w")
#     for x in range(len(data["users"])):
#         print("length of users: ", len(data["users"]))
        
#         if data['users'][x]["name"] == sys.argv[1]:
#             data['users'][x]["city"] = sys.argv[2]
#         print(data['users'][x])

#     json.dump(data,f)
    
# updatejson()

# dic={"name" : sys.argv[1], "City" : sys.argv[2]}
def appendjson(dic):
    f = open("jsoncrud.json")
    data = json.load(f)
    print(data)

    data["users"].append(dic)
    
    f = open("jsoncrud.json", "w")
    json.dump(data, f)
# appendjson(dic)


# delete json
def deletejson():
    f = open("jsoncrud.json")
    data=json.load(f)
    print(data)

    for x in data["users"]:
        print("for x: ", x)
        if x["name"] == "Kevin":
            print("Inside for x: ", x["name"])
            delectdict=x
            break
    data["users"].remove(x)
    f = open("jsoncrud.json", "w")
    json.dump(data, f)
    
# deletejson()














# data.pop("name")
# data.pop("city")
# json.dump(data, f)

