from pymongo import MongoClient

url = 'mongodb://messi:neymar123@ds253388.mlab.com:53388/heroku_v6l9bbkb?retryWrites=false'
client = MongoClient(url)
db = client['heroku_v6l9bbkb']
collection = db['test']

collection.insert_one({'a':'b'}) C

rows = collection.find({})
collection.update_one
collection.delete_one
for row in rows:
  print(row)
