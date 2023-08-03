import copy
from pymongo import MongoClient

cliente = MongoClient("mongodb://localhost:27017")

banco = cliente["projeto_api"]

estudante_col = banco["estudantes"]

def inserir_estudante(estudante):
    estudante_dict = copy.deepcopy(vars(estudante))
    estudante_col.insert_one(estudante_dict)
    return estudante_dict

def buscar_estudante(cpf):
    return estudante_col.find_one({"cpf":cpf})

def listar_todos():
    lista_estudantes = []
    cursor = estudante_col.find({})
    for documents in cursor:
        lista_estudantes.append(documents)
    return lista_estudantes
