var r = prompt("raio ");
var h = prompt("altura ");
var p = prompt("O π é: \n 1- Valor Integral \n 2- Valor Definido \n 3- Indefinido \n Respostas: ");

function areaCilindro(r, h, p){
    return 2*p*r*h + 2*p
}

switch(p){
    case 1:
        console.log(areaCilindro(r, h, math.pi));
    case 2:
        p = prompt("Qual é o valor de pi? ");
        console.log(areaCilindro(r, h, p));
    case 3:
        console.log(areaCilindro(r, h, math.pi));
    default:
        console.log("Inválido");
}