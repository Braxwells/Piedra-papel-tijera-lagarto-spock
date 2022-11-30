#Piedra, papel, tijera, lagarto y spock
import random

def jueguito(partidas): 

    jugadas = [1, 2, 3, 4, 5]
    opciones = {
        1: 'piedra',
        2: 'tijera',
        3: 'papel',
        4: 'lagarto',
        5: 'spock'
    }

    ganar = {
        1:[2, 4],
        2:[3, 4],
        3:[1, 5],
        4:[3, 5],
        5:[1, 2],
        0:[0]
    }

    while True:
        try:
            for i in range(partidas):
                jugador1 = int(input("Te enseño los movimientos: '1' piedra, '2' tijera , '3' papel, '4' lagarto o '5' spock. En caso de que quieras dejar de jugar conmigo, pulse '0' "))

                maquina = random.choice(jugadas)

                if (maquina in ganar[jugador1]):
                    print('Usted ha sacado',opciones[jugador1], 'la maquina ha elegido', opciones[maquina], 'tu ganas')

                elif jugador1 == maquina:
                    print(f'Ambos hemos sacado {opciones[jugador1]}, hemos empatado')

                elif jugador1 == 0:
                    return('Gracias por jugar conmigo.')

                else:
                    print ('Usted ha sacado',opciones[jugador1], 'la maquina ha elegido', opciones[maquina], 'tu pierdes')
            break
        except ValueError:
            print ('Empecemos de 0, por favor introduzca un número de los que pido ')

    return 'Gracias por molestarte y jugar conmigo ^^'


while True:
    try:   
        games = int(input('¿Cuántas partidas vas a querer jugar? '))
        print(jueguito(games))    
        break

    except ValueError:   
        continue         

