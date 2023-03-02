from bson.objectid import ObjectId
a = [{'_id': ObjectId('63f6af791c5757406e1f8ad1'), 'name': 'teste', 'endereco': 'teste', 'telefone': '111111', 'municipio': 'teste', 'cep': '111111', 'email': 'teste'}, {'_id': ObjectId('63f6af821c5757406e1f8ad2'), 'name': 'teste1', 'endereco': 'teste1', 'telefone': '111111', 'municipio': 'teste1', 'cep': '111111', 'email': 'teste1'}, {'_id': ObjectId('63f6af8e1c5757406e1f8ad3'), 'name': 'teste2', 'endereco': 'teste2', 'telefone': '222222', 'municipio': 'teste2', 'cep': '22222222', 'email': 'teste2'}, {'_id': ObjectId('63f6af9b1c5757406e1f8ad4'), 'name': 'teste3', 'endereco': 'teste3', 'telefone': '3333333', 'municipio': 'teste3', 'cep': '3333333', 'email': 'teste3'}]
b = []
for key in a:
    sla = str(key['_id'])
    sla = sla.replace('ObjectId', '')
    sla = sla.replace(')','')
    sla = sla.replace('(','')
    teste = {key['name']: sla}
    b.append(teste)
print(b)
# x = b.replace('ObjectId','')
# x = b.replace(')','')
# x = b.replace('(','')
# print(x)
