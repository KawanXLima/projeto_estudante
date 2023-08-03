const url = "http://127.0.0.1:8000/";

const get_estudante = function (cpf) {
  fetch(`${url}students/${cpf}`, { method: "GET" })
    .then((response) => {
      if (!response.ok) {
        throw new Error(`HTTP error ${response.status}`);
      }

      return response.json();
    })
    .then((data) => {
      console.log(data);
    });
};

function validarEstudante() {
  let valor = document.forms["fomr"]["fname"].value;
  get_estudante(valor);
}

fetch(`${url}students/`, { method: "GET" })
  .then((response) => {
    if (!response.ok) {
      throw new Error(`HTTP error ${response.status}`);
    }

    return response.json();
  })
  .then((data) => {
    console.log(data);
  });

const inserirEstudante = function (estudante) {
  const options = {
    method: "POST",
    body: JSON.stringify(estudante),
    headers: {
      "Content-type": "application/json; charset=UTF-8",
    },
  };

  fetch(`${url}students/`, options)
    .then((response) => {
      if (!response.ok) {
        throw new Error(`Http error ${response.status}`);
      }

      return response.json();
    })
    .then((data) => {
      console.log(data);
    });
};

function cadastrarEstudante() {
  let estudante = {
    id: document.forms["cadastro"]["id"].value,
    nome: document.forms["cadastro"]["nome"].value,
    cpf: document.forms["cadastro"]["cpf"].value,
    turma: document.forms["cadastro"]["turma"].value,
  };

  inserirEstudante(estudante);
}
