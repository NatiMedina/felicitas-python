def esAbecedaria(palabra):
    for i in range(len(palabra)-1):
        if palabra[i] > palabra[i+1]:
            return False
    return True

def esPar(numero):
    #numero = bin(numero)
    #ultimoDigito = numero[len(numero)-1]
    return (numero & 1) == 0

print(bin(40))
print(esPar(40))