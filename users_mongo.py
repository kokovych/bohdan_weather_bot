# -*- coding: utf-8 -*
import pymongo

def main():
    client = pymongo.MongoClient('localhost', 27017)
    db = client["telegram_weather_db"]
    collection = db['mycollection']
    print(collection)
    qs = collection.insert({"user_id": 1, "lang" : "en"})
    print(qs)
    

if __name__=="__main__":
    main()