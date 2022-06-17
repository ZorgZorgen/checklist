
// impriming una letra/string N cantidad de veces, puasando entre cada print 

function printIntervalo(letra, N, intervalo) {
    var contador = 0;
    var intervalId = establecerIntervalo(function () {
      console.log(letra);
      contador += 1;
      if (contador >= N) {
        borrarIntervalo(intervalId);
        console.log('fin de impresion', letra, N, 'veces');
      }
    }, intervalo);
  }