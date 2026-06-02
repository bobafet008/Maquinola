saldo = 5
contador = 0
continuar = True
while (saldo >= 1.5 and contador < 3 and continuar):
    print ("maquina de snacks")
    print ("1. papas : 1.50")
    print ("2. chocolate : 2.0")
    print ("3. refresco : 2.5")
    opcion = input ()
    if opcion == "salir":
        continuar = False
    else:
        if(opcion ==1 and saldo >= 1.5) or (opcion == 2 and saldo >= 2.0) or (opcion == 3 and saldo >= 2.5):
            if opcion == 1:
                saldo = saldo - 1.5
                contador = contador + 1
            elif opcion == 2:
                saldo = saldo - 2.0
                contador = contador + 1
            elif opcion == 3:
                saldo = saldo - 2.5
                contador = contador + 1
            print (saldo)
        else:
            print ("error")
print (contador)
            