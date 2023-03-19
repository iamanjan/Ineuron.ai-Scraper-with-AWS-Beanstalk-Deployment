import pymongo
import logging

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(levelname)s:%(message)s', datefmt='%d/%m/%Y %I:%M:%S %p')

class MongoOperation:
    #def __init__(self, username="YOUR_USERNAME", password="YOUR_PASSWORD"):
    def __init__(self, username="mongodb", password="mongodb"):
        try:
            self. username = username
            self.password = password
            #self.url = f"mongodb+srv://{username}:{password}@clusterofsurajit.99hrrkq.mongodb.net/?retryWrites=true&w=majority"
            #self.url=f"mongodb+srv://mongodb:mongodb@anjan.arz2abh.mongodb.net/?retryWrites=true&w=majority"
            self.url=f"mongodb://mongodb:mongodb@ac-sxvtwbp-shard-00-00.arz2abh.mongodb.net:27017,ac-sxvtwbp-shard-00-01.arz2abh.mongodb.net:27017,ac-sxvtwbp-shard-00-02.arz2abh.mongodb.net:27017/?ssl=true&replicaSet=atlas-vwuf9z-shard-0&authSource=admin&retryWrites=true&w=majority"

        except Exception as e:
            logging.error(str(e))
    
    def get_mongo_client(self):
        try:
            client = pymongo.MongoClient(self.url)
            return client
        except Exception as e:
            logging.error(str(e))
    
    def get_database(self, db_name="ineuron"):
        try:
            client = self.get_mongo_client()
            database = client[db_name]
            return database
        except Exception as e:
            logging.error(str(e))
    
    def get_collection(self, db_name="ineuron", collection_name="courses"):
        try:
            database = self.get_database(db_name)
            collection = database[collection_name]
            return collection
        except Exception as e:
            logging.error(str(e))