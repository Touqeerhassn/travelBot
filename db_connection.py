import pymongo

url = 'mongodb+srv://touqeerqfnetwork:egLjfh7Jlsq69oN6@cluster0.cruq0gs.mongodb.net/?retryWrites=true&w=majority'
client = pymongo.MongoClient(url)

db = client['test']