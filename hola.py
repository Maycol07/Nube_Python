
num=int(input("Ingrese un numero: "))
while num<0:
    print("Erro el numero deber ser positivo: ")
    num=int(input("Ingre el numero: "))

    if num!=0:
        x=1
        factorial=1
        while x<num:
            factorial=factorial*x
            x+=1
        print("El factorial es: ", factorial)

    elif num==0:
        print("El factorial es 1")