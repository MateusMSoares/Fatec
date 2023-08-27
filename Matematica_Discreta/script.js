const conjunto1 = document.getElementById("conjunto1");
const conjunto2 = document.getElementById("conjunto2");
const submitButton = document.getElementById("submit");
const output = document.getElementById("output");

submitButton.addEventListener("click", () => {
  const numerosConjunto1 = conjunto1.value
    .split(",")
    .map((elemento) => parseInt(elemento.trim()));

  const numerosConjunto2 = conjunto2.value
    .split(",")
    .map((elemento) => parseInt(elemento.trim()));

  // para testes
  //   const numerosConjunto1 = [2, 3, 4, 5];
  //   const numerosConjunto2 = [1, 4, 6, 7];

  const conjuncao = () => {
    const criaConjuncao = new Set();
    for (const elemento of numerosConjunto1) {
      if (numerosConjunto2.includes(elemento)) {
        criaConjuncao.add(elemento);
      }
    }
    console.log("Conjuncao:");
    console.log(criaConjuncao);
    return criaConjuncao;
  };

  const disjuncao = () => {
    const criaDisjuncao = new Set();
    for (const elemento of numerosConjunto1) {
      criaDisjuncao.add(elemento);
    }
    for (const elemento of numerosConjunto2) {
      criaDisjuncao.add(elemento);
    }
    console.log("Disjuncao:");
    console.log(criaDisjuncao);
    return criaDisjuncao;
  };

  const resultado = `
  <div id="resultado">
    <div id="conjuntoEntrada">
      <p>Conjunto 1: ${numerosConjunto1.join(", ")}</p>
      <p>Conjunto 2: ${numerosConjunto2.join(", ")}</p>
    </div>
    <div id="conjuntoSaida">
      <p>Conjuncao: ${Array.from(conjuncao()).join(", ")}</p>
      <p>Disjuncao: ${Array.from(disjuncao()).join(", ")}</p>
    </div>
  </div>`;

  output.innerHTML = resultado;

  conjunto1.value = "";
  conjunto2.value = "";
});
