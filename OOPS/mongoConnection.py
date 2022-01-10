import pymongo
connection_url="mongodb://localhost:27017/"
client = pymongo.MongoClient(connection_url)
db = client['users']
collection = db['employees']
# collection.insert_one({"name":"ocean"})
# collection.insert_many([{"name":"basha","number":5,"deparment":"EEE"},
# {"name":"Rajev","number":5,"deparment":"ENE"},
# {"name":"srini","number":6,"deparment":"EEE"},
# {"name":"thiru","number":5,"deparment":"ENI"}])
query = {"name":"shanmuu"}
# newData = {"$set":{"name":"shanmuu"}}

# collection.update_one(query,newData)
# ret = collection.find()
# for i in ret:
#     print(i)
collection.delete_one(query)
ret = collection.find()
for i in ret:
    print(i)


