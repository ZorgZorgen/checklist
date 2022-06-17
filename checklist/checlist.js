const asociacion = (llave, valor, objeto) => {
    objeto[llave] = valor;
  };
  
  const persona = { nombre: 'Wa;ter' };
  const resultado = asociacion('tamanoPie', 400, persona);
  
  console.log({ [persona], resultado });
  