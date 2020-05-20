import pymongo

def insert_candle(data):
	myclient = pymongo.MongoClient("mongodb://localhost:27017/")
#	print('im here')
	hd = myclient["historical_data"]
#	print('im here')
	symb = hd["reliance"];
	print(data)
	symb.insert_one(data[0]);
	print('im here')
