import random

from pip import main

def jugar(vidas):
    numero_random = random.randint(1,100)
    numero_elejido = None
    while numero_random < numero_elejido:
        numero_elejido = int(input("Ingrese un numero del 1 al 100"))

        if numero_random < numero_elejido:
           print("Te doy una pista, elije un numero mas pequeño")
           vidas -=1
        elif numero_random > numero_elejido:
           print("Te doy una pista, elije un numero mas grande")
           vidas -=1

        if vidas == 0:
            print("-----GAME OVER-----")
            print("JUEGA DE NUEVO")
            break
        print(f"te quedan vidas: ")
        if numero_random == numero_elejido:
            print("------FELICIDADES HAZ GANADO EL JUEGO------")
        
    def mai():
        while True:
            menu = """
            1 - nivel facil (10 vidas)
            2 - nivel intermedio (7 vidas)
            3 - nivel dificil (5 vidas)
            4 - salir del juego
            Elige una opcion: """

            opcion = input(menu)

            if opcion == "1":
                jugar(10)
            elif opcion == "2":
                jugar(7)
            elif opcion == "3":
                jugar(5)
            elif opcion == "4":
               print ("···SALIENDO DEL JUEGO···")
               break
            else:
                print("Opcion invalida")
                print("Elija una opcion valida y disfruta el juego")
    if __name__ == "__main__":
        main