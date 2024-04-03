import random

vida = 100
puntuacion = 0
armadura = 50

def mostrar_estado():
    print(f"Vida: {vida}\nPuntuacion: {puntuacion}\nArmadura: {armadura}\n")

def reiniciar_juego():
    global vida, puntuacion, armadura
    vida = 100
    puntuacion = 0
    armadura = 50
    
def explorar_habitacion():
    global vida
    
    enemigo_presente = random.choice([True, False])
    
    if enemigo_presente:
       print("Enemigo encontrado en la habitación!")
       hablar_con_profesor()
    else:
        print("Habitación vacía. Sigue explorando") 
        
def hablar_con_profesor():
    global vida, puntuacion
    
    print("Te encuentras con un profesor de matemáticas en la habitación.")
    print("El profesor te pregunta por las tablas de multiplicar.")
    
    respuesta_correcta = False
    
    while not respuesta_correcta and vida > 0:
        
        multiplicador = random.randint(1,10)
        multiplicando = random.randint(1,10)
        resultado_esperado = multiplicador * multiplicando
        
        respuesta = input(f"¿Cuanto es {multiplicador} x {multiplicando}? ")
        if respuesta.isdigit() and int(respuesta) == resultado_esperado:
            print("Respuesta correcta! El profesor está impresionado y te da 20 puntos.")
            puntuacion += 20
            respuesta_correcta = True
        else:
            print("Respuesta incorrecta, perdiste 10 de vida. El profesor te dá otra oportunidad.")
            vida -= 10
            
def evento_aleatorio():
    
    global vida, puntuacion, armadura
    
    evento = random.choice(["Encontraste un cofre con tesoros.", "Te caiste y perdiste algo de vida.","Descubriste un atajo seguro."])
    
    if evento == "Encontraste un cofre con tesoros.":
        print("Encontraste un cofre con tesoros. Obtuviste 20 puntos.")
        puntuacion += 20
    elif evento == "Te caiste y perdiste algo de vida.":
        print("Te caiste y perdiste algo de vida. Perdiste 10 de vida y 10 de armadura...")
        armadura -= 10
        vida -= 10
    elif evento == "Descubriste un atajo seguro.":
        print("Descubriste un atajo seguro que te lleva a la habitación del jefe final.")
        jugar_piedra_papel_tijera()
        
def jugar_piedra_papel_tijera():
    
    global puntuacion
    
    print("\n Has llegado a la habitación del jefe final.")
    print("\nTe desafía a jugar piedra, papel o tijera.")
    
    opciones = ["piedra", "papel", "tijera"]
    
    while True:
        eleccion_del_jugador = input("Elije una opción (piedra/papel/tijera): ".lower)
        eleccion_jefe = random.choice(opciones)
        
        print(f"El jefe elige {eleccion_jefe}")
        
        if eleccion_del_jugador == eleccion_jefe:
            print("Es un empate, intentalo de nuevo.")
            
        elif (eleccion_del_jugador == "piedra" and eleccion_jefe == "tijera") or \
            (eleccion_del_jugador == "papel" and eleccion_jefe == "piedra") or \
            (eleccion_del_jugador == "tijera" and eleccion_jefe == "papel"):
                print("Ganaste al jefe final!")
                puntuacion += 100
                print("Has terminado el juego.")
                break
        else:
            print("Perdiste. El jefe final te ha derrotado...")
            print("El juego comenzará de nuevo.")
            reiniciar_juego()
            break
            
    
def jugar_juego():
    
    while vida > 0:
        
        print("\n Te encuentras en un pasillo del castillo.")
        mostrar_estado()
        opcion = int(input("¿Que deseas hacer? \n1. Entrar en una habitación.\n2. Seguir explorando.\n3. Consultar tu estado.\n4. Salir del juego.\nElije una opción(1/2/3/4)."))
        if opcion == 1:
            explorar_habitacion()
        elif opcion == 2:
            evento_aleatorio()
        elif opcion == 3:
            mostrar_estado()
        elif opcion == 4:
            print("Decidiste salir del juego.")
            break
        else:
            print("Opción no válida, elije 1, 2, 3 o 4.")
            
        if vida <= 0:
            print("\nHas perdido tu personaje ha quedado sin vida.")
        elif puntuacion >= 100:
            print("\nFelicidades! Has ganado el juego!.")
            mostrar_estado()
            break
        elif armadura <= 0:
            print("\nTe has quedado sin armadura. Has perdido el juego...")
            mostrar_estado()
            break
        
jugar_juego()