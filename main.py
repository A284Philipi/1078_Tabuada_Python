numero = int(input())
cont = int(1)
while (cont <= 10):
    multiplo = int(numero * cont)
    print("{} x {} = {}".format(cont, numero, multiplo))
    cont = cont + 1