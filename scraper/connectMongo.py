from pymongo import MongoClient 

class Dict2Mongo:
    
    def __init__(self, dict, collection):
        print(collection)
        self.dict = dict

        try:
            print('Conectando a MongoDB...')
            self.client = MongoClient("mongodb+srv://admin:")
            
        except Exception as e:
            print (e)
    
        self.db = self.client.invertirOnline
        collection = self.db[collection]
        
        print(f'Ingestando data en mongoDB.invertirOnline.{collection}')

        #print(self.mycollection)
        #print(self.client['invertirOnline'].accion) 
        #dict2Mongo = collection.insert(dict)
        contador = 0
        for x in self.dict:
            contador +=1
            collection.insert(dict[x])
               
        print(f'Se agregaron {contador} registros en collection {collection}')

        
    




