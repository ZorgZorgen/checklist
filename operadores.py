def es_par(list1):
    num_par = []
    for n in list1:
        if n % 2 == 0:
            num_par.append(n)
    #retornar una lista
    return num_par

# pasar la lista a la funcion
num_par = es_par([2, 3, 42, 51, 62, 70, 5, 9])
print("Los numeros pares son:", num_par)