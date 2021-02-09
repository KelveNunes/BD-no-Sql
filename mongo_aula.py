#importando o mongo
from pymongo import MongoClient

conn = MongoClient('localhost', 27017)

#criando o banco de dados cadastrodb

db = conn.cadastrodb

#criando uma colection
# Uma coleção é um grupo de documentos armazenados no MongoDB

collection = db.cadastrodb

import datetime

post2 = {"codigo": "ID-2209876",
        "prod_name": "Televisor",
        "marcas": ["samsung", "panasonic", "lg"],
        "data_cadastro": datetime.datetime.utcnow()}

post1 = {"codigo": "ID-9987725",
        "prod_name": "Geladeira",
        "marcas": ["brastemp", "consul", "elecrolux"],
        "data_cadastro": datetime.datetime.utcnow()}

#criando uma coleção
collection = db.posts
post_id = collection.insert_one(post1)
post_id.inserted_id

collection = db.posts
post_id = collection.insert_one(post2).inserted_id

# A função find() retorna um cursor e podemos então navegar pelos dados
print(collection.find_one({"prod_name": "Televisor"}))
for post in collection.find():
    print(post)

#retorna o nome do banco
print(db.name)

#listando as coleções disponiveis
print(db.list_collection_names())



