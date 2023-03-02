from flask import Flask, make_response, jsonify, request
from pymongo import MongoClient
from bson.json_util import dumps, loads
from bson.objectid import ObjectId
from flask_cors import CORS
import json

app = Flask(__name__)
CORS(app)

# Connection with mongodb database
client = MongoClient("localhost", 27017)
db = client.agua

# Connection with mongodb collections
collection = db['clientes']
exame = db["exames"]
resultado = db["resultados"]
parametro = db["parametros"]
conta = db["contas"]

# CRUD FOR CLIENTES
@app.route('/clientes', methods=['GET'])
def get_All_clientes():
    cursor = collection.find({})
    list_cur = list(cursor)
    json_data = dumps(list_cur)
    return json_data

@app.route('/cliente/<id>', methods=['GET'])
def get_One_collections(id):
    cursor = collection.find_one({"_id": ObjectId(id)})
    json_data = dumps(cursor)
    return json_data

@app.route('/add/cliente', methods=['POST'])
def create_cliente():
    form_data = request.json
    print(form_data)
    a = collection.insert_one(form_data)
    return get_One_collections(form_data['_id'])

@app.route('/att/cliente', methods=['PUT'])
def update_One_cliente():
    form_data = request.json
    id = form_data['_id']['$oid']
    form_data.pop('_id')
    filter = {"_id": ObjectId(id)}
    cursor = collection.update_one(filter, {"$set": form_data})
    return get_One_collections(id)

@app.route('/delete/cliente/<id>', methods=['DELETE'])
def delete_One_cliente(id):
    filter = {"_id": ObjectId(id)}
    cursor = collection.delete_one(filter)
    return get_One_collections(id)


# CRUD FOR EXAMES
@app.route('/exames', methods=['GET'])
def get_All_exames():
    cursor = exame.find({})
    list_cur = list(cursor)
    json_data = dumps(list_cur)
    return json_data

@app.route('/exame/<id>', methods=['GET'])
def get_One_exame(id):
    cursor = exame.find_one({"_id": ObjectId(id)})
    json_data = dumps(cursor)
    return json_data

@app.route('/add/exame', methods=['POST'])
def create_exame():
    form_data = request.json
    a = exame.insert_one(form_data)
    return get_One_exame(form_data['_id'])

@app.route('/att/exame', methods=['PUT'])
def update_One_exame():
    form_data = request.json
    id = form_data['_id']['$oid']
    form_data.pop('_id')
    filter = {"_id": ObjectId(id)}
    cursor = exame.update_one(filter, {"$set": form_data})
    return get_One_exame(id)

@app.route('/delete/cliente', methods=['DELETE'])
def delete_One_exame():
    form_data = request.json
    id = form_data['_id']['$oid']
    filter = {"_id": ObjectId(id)}
    cursor = exame.delete_one(filter)
    return get_One_exame(id)


# CRUD FOR RESULTADOS
@app.route('/resultados', methods=['GET'])
def get_All_resultados():
    cursor = resultado.find({})
    list_cur = list(cursor)
    json_data = dumps(list_cur)
    return json_data

@app.route('/resultado/<id>', methods=['GET'])
def get_One_resultado(id):
    cursor = resultado.find_one({"_id": ObjectId(id)})
    json_data = dumps(cursor)
    return json_data

@app.route('/add/resultado', methods=['POST'])
def create_resultado():
    form_data = request.json
    a = resultado.insert_one(form_data)
    return get_One_resultado(form_data['_id'])

@app.route('/att/resultado', methods=['PUT'])
def update_One_resultado():
    form_data = request.json
    id = form_data['_id']['$oid']
    form_data.pop('_id')
    filter = {"_id": ObjectId(id)}
    cursor = resultado.update_one(filter, {"$set": form_data})
    return get_One_resultado(id)

@app.route('/delete/resultado', methods=['DELETE'])
def delete_One_resultado():
    form_data = request.json
    id = form_data['_id']['$oid']
    filter = {"_id": ObjectId(id)}
    cursor = resultado.delete_one(filter)
    return get_One_resultado(id)


# CRUD FOR PARAMETROS
@app.route('/parametros', methods=['GET'])
def get_All_parametros():
    cursor = parametro.find({})
    list_cur = list(cursor)
    json_data = dumps(list_cur)
    return json_data

@app.route('/parametro/<id>', methods=['GET'])
def get_One_parametro(id):
    cursor = parametro.find_one({"_id": ObjectId(id)})
    json_data = dumps(cursor)
    return json_data

@app.route('/add/parametro', methods=['POST'])
def create_parametro():
    form_data = request.json
    a = parametro.insert_one(form_data)
    return get_One_parametro(form_data['_id'])

@app.route('/att/parametro', methods=['PUT'])
def update_One_parametro():
    form_data = request.json
    id = form_data['_id']['$oid']
    form_data.pop('_id')
    filter = {"_id": ObjectId(id)}
    cursor = parametro.update_one(filter, {"$set": form_data})
    return get_One_parametro(id)

@app.route('/delete/parametro', methods=['DELETE'])
def delete_One_parametro():
    form_data = request.json
    id = form_data['_id']['$oid']
    filter = {"_id": ObjectId(id)}
    cursor = parametro.delete_one(filter)
    return get_One_parametro(id)


# CRUD FOR CONTAS
@app.route('/contas', methods=['GET'])
def get_All_contas():
    cursor = conta.find({})
    list_cur = list(cursor)
    json_data = dumps(list_cur)
    return json_data

@app.route('/clients', methods=['GET'])
def get_All_name_contas():
    cursor = collection.find({})
    list_cur = list(cursor)
    nomes = []
    for key in list_cur:
        sla = str(key['_id'])
        sla = sla.replace('ObjectId', '')
        sla = sla.replace(')', '')
        sla = sla.replace('(', '')
        data = {"nome": key['name'],"id": sla}
        nomes.append(data)
    json_data = dumps(nomes)
    return json_data

@app.route('/conta/<id>/<senha>', methods=['GET'])
def get_conta(id, senha):
    cursor = conta.find_one({"usuario": id})
    json_data = dumps(cursor)
    data = json.loads(json_data)
    if data != None:
        if data["usuario"] == id:
            if data["senha"] == senha:
                return {"usuario": 'True', "senha": 'True', "type": data["type"]}
            else:
                return {"usuario": 'True', "senha": 'False'}
    else:
        return {"usuario": 'False', "senha": 'False'}

@app.route('/conta/<id>', methods=['GET'])
def get_One_conta(id):
    cursor = conta.find_one({"_id": ObjectId(id)})
    json_data = dumps(cursor)
    return json_data

@app.route('/add/conta', methods=['POST'])
def create_conta():
    form_data = request.json
    a = conta.insert_one(form_data)
    return get_One_conta(form_data['_id'])

@app.route('/att/conta', methods=['PUT'])
def update_One_conta():
    form_data = request.json
    id = form_data['_id']['$oid']
    form_data.pop('_id')
    filter = {"_id": ObjectId(id)}
    cursor = conta.update_one(filter, {"$set": form_data})
    return get_One_conta(id)

@app.route('/delete/conta', methods=['DELETE'])
def delete_One_conta():
    form_data = request.json
    id = form_data['_id']['$oid']
    filter = {"_id": ObjectId(id)}
    cursor = conta.delete_one(filter)
    return get_One_conta(id)


app.run(debug=True)