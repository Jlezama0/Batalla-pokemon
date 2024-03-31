import random
import os
import time
#------------------------------------------------------------------------------------------  
#Definicion de clases para los ataques de cada pokemon  
class IattackBehavior:
    def attacks(self):
        pass

class Pikachu_Attacks(IattackBehavior):
    def attacks(self):
        attacks = {
            'Impactrueno': 40,
            'Rayo': 50,
            'Ataque Rápido': 30,
            'Placaje': 20
        }
        return attacks

class Caterpie_Attacks(IattackBehavior):
    def attacks(self):
        attacks = {
            'Placaje': 10,
            'Tacleada': 15,
            'Supersónico': 10,
            'Drenadoras': 20
        }
        return attacks

class Pidgeotto_Attacks(IattackBehavior):
    def attacks(self):
        attacks = {
            'Picotazo': 25,
            'Remolino': 30,
            'Tornado': 35,
            'Ataque Rápido': 30
        }
        return attacks

class Bulbasaur_Attacks(IattackBehavior):
    def attacks(self):
        attacks = {
            'Látigo Cepa': 30,
            'Drenadoras': 20,
            'Placaje': 15,
            'Somnífero': 25
        }
        return attacks

class Charmander_Attacks(IattackBehavior):
    def attacks(self):
        attacks = {
            'Lanzallamas': 40,
            'Gruñido': 10,
            'Arañazo': 20,
            'Ascuas': 30
        }
        return attacks

class Squirtle_Attacks(IattackBehavior):
    def attacks(self):
        attacks = {
            'Pistola Agua': 35,
            'Burbuja': 25,
            'Ataque Rápido': 20,
            'Placaje': 15
        }
        return attacks

class Krabby_Attacks(IattackBehavior):
    def attacks(self):
        attacks = {
            'Burbuja': 20,
            'Rayo Burbuja': 25,
            'Placaje': 15,
            'Tajo Cruzado': 30
        }
        return attacks

class Raticate_Attacks(IattackBehavior):
    def attacks(self):
        attacks = {
            'Hipercolmillo': 45,
            'Ataque Rápido': 25,
            'Placaje': 20,
            'Golpe Cabeza': 35
        }
        return attacks

class Muk_Attacks(IattackBehavior):
    def attacks(self):
        attacks = {
            'Lodo': 30,
            'Bomba Lodo': 35,
            'Ataque Ácido': 25,
            'Infortunio': 20
        }
        return attacks

class Kingler_Attacks(IattackBehavior):
    def attacks(self):
        attacks = {
            'Hidropulso': 40,
            'Rayo Burbuja': 30,
            'Rayo': 35,
            'Placaje': 25
        }
        return attacks

#---------------------------------------------------------------------------------------------------
#Definicion de la clase principal Pokemon y las clases de cada pokemon
class pokemon:
    def __init__(self, attackBehaviors:IattackBehavior) -> None:
        self.attackBehaviors=attackBehaviors
        

    def perform_attack(self):
        info_attacks={}
        info_attacks=self.attackBehaviors.attacks()
        return info_attacks

class pikachu(pokemon):
    def __init__(self) -> None:
        super().__init__(Pikachu_Attacks())
        self.health = 50

class caterpie(pokemon):
    def __init__(self) -> None:
        super().__init__(Caterpie_Attacks())
        self.health = 35

class pidgeotto(pokemon):
    def __init__(self) -> None:
        super().__init__(Pidgeotto_Attacks())
        self.health = 63

class bulbasaur(pokemon):
    def __init__(self) -> None:
        super().__init__(Bulbasaur_Attacks())
        self.health = 70

class charmander(pokemon):
    def __init__(self) -> None:
        super().__init__(Charmander_Attacks())
        self.health = 80

class squirtle(pokemon):
    def __init__(self) -> None:
        super().__init__(Squirtle_Attacks())
        self.health = 75

class krabby(pokemon):
    def __init__(self) -> None:
        super().__init__(Krabby_Attacks())
        self.health = 30

class raticate(pokemon):
    def __init__(self) -> None:
        super().__init__(Raticate_Attacks())
        self.health = 35

class muk(pokemon):
    def __init__(self) -> None:
        super().__init__(Muk_Attacks())
        self.health = 105

class kingler(pokemon):
    def __init__(self) -> None:
        super().__init__(Kingler_Attacks())
        self.health = 55

#-------------------------------------------------------------------------------------------------------
#Funcion para limpiar la consola
def limpiar_consola():
    os.system('cls')  

#Funcion jugador: Esta funcion devuelve el nombre del jugador, la lista de sus pokemones y el 
#indice de esos pokemones en la lista principal de pokemones.
def player(pokemones:list):

    player_name=input('Ingresa tu nombre para la batalla: ').upper()
    limpiar_consola()
    pokemons_player=[]
    index_pokemons_player=[]

    print(f'Preparate para la batalla {player_name} elige 3 pokemones:\n')
    
    for i in range(3):
        def selection_player():
            for i in range(len(pokemones)):
                if pokemones[i] not in pokemons_player:
                    print(f'{i+1}.{pokemones[i]}')    
            while True:
                choise_player=int(input('\nEscribe el numero del pokemon que deseas elegir: '))
                limpiar_consola()
                if choise_player in range(len(pokemones)):
                    break
                    
                else:
                    print('Opción no válida. Por favor, elige un Pokémon válido.')
                    time.sleep(1)
                    choise_player=selection_player()
                    break
            return choise_player
        
        select_player=selection_player()
        pokemons_player.append(pokemones[select_player-1])
        index_pokemons_player.append(select_player-1)
        

    return player_name,pokemons_player,index_pokemons_player

#Funcion maquina: Esta funcion devuelve la lista de sus pokemones y el 
#indice de esos pokemones en la lista principal de pokemones.
def machine(pokemones:list):

    pokemons_machine=[]
    index_pokemons_machine=[]

    while len(pokemons_machine) < 3:
        machine_choise= random.choice(pokemones)
        if machine_choise not in pokemons_machine:
            pokemons_machine.append(machine_choise)
            index_pokemons_machine.append(pokemones.index(machine_choise))


    
    return pokemons_machine,index_pokemons_machine

#Una vez el jugador y la maquina eligieron sus equipos, las funciones 
#teamPlayer y teamMachine devulve un diccionario de los pokemones selccionados y su vida base.
def teamPlayer(object_pokemons,index_pokemones_player,pokemons_player1:list):

    team_player1={}
        
    #print('Tus pokemones:')

    for pokemon, index_pokemon in zip(range(len(pokemons_player1)),range(len(index_pokemones_player))) :
        team_player1[pokemons_player1[pokemon]]=object_pokemons[index_pokemones_player[index_pokemon]].health
        #print(f'{pokemon+1}.{pokemons_player1[pokemon]}, salud: {object_pokemons[index_pokemones_player[index_pokemon]].health}')

    return team_player1

def teamMachine(object_pokemons,index_pokemons_machine,pokemons_machine:list):

    team_machine={}
        
    for pokemon, index_pokemon in zip(range(len(pokemons_machine)),range(len(index_pokemons_machine))) :

        team_machine[pokemons_machine[pokemon]]=object_pokemons[index_pokemons_machine[index_pokemon]].health
    
    return team_machine

#Funcion ataque del jugador: Devuelve un diccionario con el ataque que eligio el jugador del pokemon seleccionado.
def attackPlayer(object_pokemons,index_pokemones_player,team_player1):
            
        
        attack={}
        chosen_pokemon=''
                    
        
        while True:
            choisePokemon=int(input('\nElige el numero de tu pokemon para atacar: '))-1
            
            if choisePokemon in range(len(list(team_player1.keys()))):
                limpiar_consola()
                break
            else:
                print('Opción no válida. Por favor, elige un Pokémon válido.')
        
        pokemon_keys=list(team_player1.keys())
        chosen_pokemon=pokemon_keys[choisePokemon] 
        attacks=object_pokemons[index_pokemones_player[choisePokemon]].perform_attack()
        
        print(f"Estos son los ataques de {chosen_pokemon}:\n ")
        for a, att in enumerate(attacks, start=1):
            print(f'{a}.{att}: {attacks[att]}')    

        while True:
            num_attack=int(input('\nElige el numero del ataque que deseas realizar: '))-1
            
            if num_attack in range(len(list(attacks.keys()))):
                limpiar_consola()
                break
            else:
                print('Opción no válida. Por favor, elige un Ataque válido.\n')
        

        aux=list(attacks.keys())
        
        attack[aux[num_attack]] = attacks[aux[num_attack]]

        return chosen_pokemon,attack

#Funcion ataque de la maquina: Devuelve un diccionario con el ataque que eligio la maquina del pokemon seleccionado.
def attackMachine(object_pokemons,index_pokemones_machine,team_machine):
            
        
        attack_machine={}
                    
        pokemon_keys=list(team_machine.keys()) 
        
        chosen_Pokemon=random.choice(pokemon_keys)
        
        attacks=object_pokemons[index_pokemones_machine[pokemon_keys.index(chosen_Pokemon)]].perform_attack()
        
        aux=list(attacks.keys())
        
        attack=random.choice(aux)
        
        attack_machine[attack] = attacks[attack]

        return chosen_Pokemon,attack_machine

#Funcion batalla: En esta funcion se desarrolla todo el combate entre el jugador y la maquina.
def battle(object_pokemons, index_pokemones_player,index_pokemons_machine, pokemons_player1: list,player_name, pokemons_player2: list):

    print('Es hora de la batalla!!!\n')

    #Lamamos los equipos del jugador y la maquina
    team_player = teamPlayer(object_pokemons, index_pokemones_player, pokemons_player1)
    team_machine=teamMachine(object_pokemons,index_pokemons_machine,pokemons_player2)
    turn = 1  # Inicializamos el turno con el jugador 1

    #El bucle termina si la lista de pokemones del jugador o la maquina llega a 0.
    while len(pokemons_player1) > 0 and len(pokemons_player2) > 0:
        
        if turn == 1:

            pok_player = team_player

            print('Tu turno.')
            print('Tus pokemones:\n')

            #Se muestran los pokemones del jugador
            for p, pok in enumerate(pok_player, start=1):
                print(f'{p}.{pok}: {pok_player[pok]}')

            #Llamamos a attackPlayer para saber cual pokemon eligio para atacar y su ataque.
            chosen_Pokemon_player, attack_player = attackPlayer(object_pokemons, index_pokemones_player, pok_player)

            #Se muestra al equipo rival
            print('Equipo rival:\n')
            for r, rival in enumerate(team_machine, start=1):
                print(f'{r}.{rival}: {team_machine[rival]}')

            # Solicitar al jugador que elija al Pokémon rival para atacar
            while True:
                chosen_rival = int(input('\nElige al Pokémon rival que quieres atacar: ')) - 1
                limpiar_consola()
                if chosen_rival in range(len(pokemons_player2)):
                    break
                else:
                    print('Opción no válida. Por favor, elige un Pokémon válido.')

            #Se actualiza la vida de los pokemones de la maquina luego del ataque
            c=list(attack_player.keys())
            team_machine[pokemons_player2[chosen_rival]]= team_machine[pokemons_player2[chosen_rival]] -(attack_player[c[0]]/2)

            # Se muestra el ataque del jugador
            print(f'Ataque del Jugador {player_name}:\n {chosen_Pokemon_player} realiza {c[0]} contra {pokemons_player2[chosen_rival]}')
            time.sleep(4)
            limpiar_consola()

            #Comprueba si algun pokemon del equipo rival fue derrotado y si es asi, lo elimina.
            team_machine_values=list(team_machine.values())
            for sear in range(len(team_machine_values)):
                if team_machine_values[sear] <= 0:
                    eliminate=team_machine_values.index(team_machine_values[sear])
                    print(f'¡El Pokémon rival {pokemons_player2[eliminate]} ha sido derrotado!')
                    time.sleep(2)
                    limpiar_consola()
                    del team_machine[pokemons_player2[eliminate]]
                    pokemons_player2.remove(pokemons_player2[eliminate])
                    break

            # Cambiamos el turno al jugador 2
            turn = 2
        else:
            print('TURNO DE LA MAQUINA\n')
            chosen_Pokemon_machine, attack_machine = attackMachine(object_pokemons, index_pokemons_machine, team_machine)

            # Solicitar a la maquina que elija al Pokémon rival para atacar
            aux=list(pok_player.keys())
            chosen_rival = random.choice(aux)

            #Se actualiza la vida de los pokemones del jugador luego del ataque
            d=list(attack_machine.keys())
            pok_player[chosen_rival]= pok_player[chosen_rival]-(attack_machine[d[0]]/2)
                
            # Se muestra el ataque de la maquina
            print(f'Ataque de la maquina: \n{chosen_Pokemon_machine} realiza {d[0]} contra {chosen_rival}.')
            time.sleep(4)
            limpiar_consola()
            
            #Comprueba si algun pokemon del equipo del jugador principal fue derrotado y si es asi, lo elimina.
            pok_player_values=list(pok_player.values())
            for search in range(len(pok_player_values)):
                if pok_player_values[search] <= 0:
                    eliminate=pok_player_values.index(pok_player_values[search])
                    print(f'¡Tu Pokemon {pokemons_player1[eliminate]} ha sido derrotado!')
                    time.sleep(2)
                    limpiar_consola()
                    del pok_player[pokemons_player1[eliminate]]
                    pokemons_player1.remove(pokemons_player1[eliminate])
                    break
            
            # Cambiamos el turno al jugador 1
            turn = 1

    if len(pokemons_player1) == 0:
        print('Haz perdido.')
    elif len(pokemons_player2) == 0:
        print('¡Felicidades! Has ganado.')

#Funcion principal del juego
def game(object_pokemons):

    pokemones=['Pikachu','Caterpie','Pidgeotto','Bulbasaur','Charmander','Squirtle','Krabby','Raticate','Muk','Kingler']

    print("BIENVENIDO A BATALLA POKEMON:")
    #Se pide el numero de jugadores
    num_players_str=input("Ingrese el numero de jugadores(1 o 2):")
    limpiar_consola()

    try:
        num_players=int(num_players_str)
    except:
        print('Ingrese un numero entero valido.')
        time.sleep(1)
        limpiar_consola()
        game(object_pokemons)
        
    else:
        if num_players not in [1,2] :
            print('El numero de jugadores ingresados es incorrecto.')
            time.sleep(1)
            limpiar_consola()
            game(object_pokemons)
            
            return
        
        if num_players == 2 :
            print('Aun esta en desarrollo, pero puedes intentarlo contra la maquina!')
            time.sleep(2)
            limpiar_consola()
            game(object_pokemons)
            
        else:
            #Llamamos a player y machine para saber la informacion de cada uno y se llama a battle para saber quien fue 
            #el ganador.
            player1_name,pokemons_player1,index_pokemons_player1=player(pokemones)
            pokemons_machine,index_pokemons_machine=machine(pokemones)
            battle(object_pokemons,index_pokemons_player1,index_pokemons_machine,pokemons_player1,player1_name,pokemons_machine)

if __name__=="__main__":

    Pikachu=pikachu()
    Caterpie=caterpie()
    Pidgeotto=pidgeotto()
    Bulbasaur=bulbasaur()
    Charmander=charmander()
    Squirtle=squirtle()
    Krabby=krabby()
    Raticate=raticate()
    Muk=muk()
    Kingler=kingler()

    object_pokemons=[Pikachu,Caterpie,Pidgeotto,Bulbasaur,Charmander,Squirtle,Krabby,Raticate,Muk,Kingler]

    #Iniciamos el juego
    game(object_pokemons)