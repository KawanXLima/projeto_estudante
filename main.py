from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Dict
import db as mongodb

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


db: Dict[str, Dict] = {}


class Student(BaseModel):
    cpf: str
    id: int
    nome: str
    turma: str

@app.get("/")
def get_root():
    return {"ola":"mundo"}

@app.post("/students/", response_model=Student)
def create_student(student: Student):
   estudante_dict = mongodb.inserir_estudante(student)
   return estudante_dict


@app.get("/students/{cpf}", response_model=Student)
def read_student(cpf: str):
    return mongodb.buscar_estudante(cpf)


@app.get("/students/", response_model=List[Student])
def read_students():
    return mongodb.listar_todos()


@app.put("/students/{cpf}", response_model=Student)
def update_student(cpf: str, student: Student):
    if cpf not in db:
        raise HTTPException(status_code=404, detail="Estudante não encontrado.")
    db[cpf] = student.dict()
    return db[cpf]


@app.delete("/students/{cpf}", response_model=Student)
def delete_student(cpf: str):
    if cpf not in db:
        raise HTTPException(status_code=404, detail="Estudante não encontrado.")
    deleted_student = db.pop(cpf)
    return deleted_student
