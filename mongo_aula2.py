import pymongo

#criando a conexão com o mongo DB(padrão)
cliente_conn = pymongo.MongoClient()

#listando os bancos de dados disponiveis

print(cliente_conn.list_database_names())

#definindo o obejeto DB

db = cliente_conn.cadastrodb

#listando as conexões do objeto DB

print(db.list_collection_names())

#criando uma coleção

#db.create_collection('mycollection')

#listando as conexões

print(db.list_collection_names())

#inserindo um documento na coleção

db.mycollection.insert_one({
   'titulo': 'MongoDB com Python',
   'descricao': 'MongoDB é um Banco de Dados NoSQL',
   'by': 'Data Science Academy',
   'url': 'http://www.datascienceacademy.com.br',
   'tags': ['mongodb', 'database', 'NoSQL'],
   'likes': 100
})

#retornando o documento criado

print(db.mycollection.find_one())

#preparando um documento

doc1 = {"Nome":"Donald","sobrenome":"Trump","twitter":"@POTUS"}
doc2 = {"Site":"http://www.datascienceacademy.com.br",
        "facebook":"facebook.com/dsacademybr"}
#adcionando elemento no docuemnto

#db.mycollection.insert_one(doc1)
db.mycollection.insert_one(doc2)
#retonadado elementos do documento
for element in db.mycollection.find():
    print(element)


