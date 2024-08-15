#instruccion
print("vamos a ordenar tres numeros")

#pidiendo los numeros

numero1 = int(input("Ingrese el primer numero: \n"))
numero2 = int(input("Ingrese el segundo numero: \n"))
numero3 = int(input("Ingrese el tercer numero: \n"))


#creando una lista

numeros = [numero1,numero2,numero3]

#ordenando lista 
numeros.sort(reverse=True)

#imprimiendo resultados
print("Tus numeros ordenados de mayor a menor son: " , numeros)