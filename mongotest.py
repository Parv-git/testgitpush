import pymongo

client = pymongo.MongoClient(
    "mongodb+srv://paravsharma:peAkeWVrLVMubF9U@cluster0.7dpp5gj.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)

d = {
    'name': 'Parav',
    'email': 'paravsharma101@gmail.com',
    'surname': 'Sharma'
}

db1 = client['mongotest']
coll = db1['test']
coll.insert_one(d)



