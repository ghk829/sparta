from pymongo import MongoClient

url = 'mongodb://messi:neymar123@ds253388.mlab.com:53388/heroku_v6l9bbkb?retryWrites=false'
client = MongoClient(url)
db = client['heroku_v6l9bbkb']
collection = db['test']

rows = collection.find()

result = [] # 리스트를 통해서 잠시 저장한다.

for row in rows:
   if 'age' in row:
       if row['age'] > 21:
          result.append(row['age'])

max_age = max(result)

rows = collection.find()

for row in rows:
   if 'age' in row:
       if row['age'] == max_age:
          print(row)