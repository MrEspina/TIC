def bucles_while():
    suma=0
    continuar='a' 
    while(continuar=='a'):
        num=input("introduce un numero: ")
        suma=suma+num
        continuar=raw_input("Quieres leer un numero m�s (a/N):")
    print("SUMA= "+str(suma))
bucles_while()
