import random
#------------------------------------------------------------------------------------------    
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
def player(pokemones:list):

    player_name=input('Ingresa tu nombre para la batalla: ').upper()
    pokemons_player=[]
    index_pokemons_player=[]

    print(f'Preparate para la batalla {player_name} elige 3 pokemones:')
    
    #while len(pokemons_player1)< 4:
    for i in range(3):
        aux=0
        for i in range(len(pokemones)):
            if pokemones[i] not in pokemons_player:
                print(f'{i+1}.{pokemones[i]}')    

        choise_player=int(input('Escribe el numero del pokemon que deseas elegir: '))
        pokemons_player.append(pokemones[choise_player-1])
        index_pokemons_player.append(choise_player-1)

    return player_name,pokemons_player,index_pokemons_player

def machine(pokemones:list):

    pokemons_machine=[]
    index_pokemons_machine=[]

    while len(pokemons_machine) < 3:
        machine_choise= random.choice(pokemones)
        if machine_choise not in pokemons_machine:
            pokemons_machine.append(machine_choise)
            index_pokemons_machine.append(pokemones.index(machine_choise))

    return pokemons_machine,index_pokemons_machine



def teamPlayer(object_pokemons,index_pokemones_player,pokemons_player1:list):

    team_player1={}
        
    print('Tus pokemones:')

    for pokemon, index_pokemon in zip(range(len(pokemons_player1)),range(len(index_pokemones_player))) :
        team_player1[pokemons_player1[pokemon]]=object_pokemons[index_pokemones_player[index_pokemon]].health
        #print(f'{pokemon+1}.{pokemons_player1[pokemon]}, salud: {object_pokemons[index_pokemones_player[index_pokemon]].health}')

    aux=list(team_player1.keys())
    for i in range(len(aux)):
        print(f'{i+1}.{aux[i]}')

    return team_player1

def teamMachine(object_pokemons,index_pokemones_player,pokemons_machine:list):

    team_machine={}
        
    for pokemon, index_pokemon in zip(range(len(pokemons_machine)),range(len(index_pokemones_player))) :

        team_machine[pokemons_machine[pokemon]]=object_pokemons[index_pokemones_player[index_pokemon]].health
        
    return team_machine


def attackPlayer(object_pokemons,index_pokemones_player,team_player1):
            
        
        attack={}
        chosen_pokemon=''
                    
        choisePokemon=int(input('Elige el numero de tu pokemon para atacar: '))-1
        
        pokemon_keys=list(team_player1.keys())
        chosen_pokemon=pokemon_keys[choisePokemon] 
        
        attacks=object_pokemons[index_pokemones_player[choisePokemon]].perform_attack()
        
        
        print(f"Estos son los ataques de {chosen_pokemon}: ")
        for a, att in enumerate(attacks, start=1):
            print(f'{a}.{att}: {attacks[att]}')    
        num_attack=int(input('Elige el numero del ataque que deseas realizar: '))-1

        aux=list(attacks.keys())
        
        attack[aux[num_attack]] = attacks[aux[num_attack]]

        return chosen_pokemon,attack
        
def attackMachine(object_pokemons,index_pokemones_machine,team_machine):
            
        
        attack_machine={}
                    
        pokemon_keys=list(team_machine.keys()) 
        chosen_Pokemon=random.choice(pokemon_keys)
        
        attacks=object_pokemons[index_pokemones_machine[pokemon_keys.index(chosen_Pokemon)]].perform_attack()
            
        aux=list(attacks.keys())
        
        attack=random.choice(aux)
        
        
        attack_machine[attack] = attacks[attack]

        return chosen_Pokemon,attack_machine

def battle(object_pokemons,index_pokemones_player,pokemons_player1:list, pokemons_player2:list):

    print('Es hora de la batalla!!!')
    

    while len(pokemons_player1) > 0 or len(pokemons_player2) > 0:

        if len(pokemons_player1) == 0:
            print('Haz perdido.')
            break
        else:

            team_player=teamPlayer(object_pokemons,index_pokemones_player,pokemons_player1)
            chosen_Pokemon_player,attack_player=attackPlayer(object_pokemons,index_pokemones_player,team_player)

            team_machine=teamMachine(object_pokemons,index_pokemones_player,pokemons_player2)
            chosen_Pokemon_machine,attack_machine=attackMachine(object_pokemons,index_pokemones_player,team_machine)

            print('Equipo rival:')

            for r, rival in enumerate(team_machine, start=1):
                print(f'{r}.{rival}: {team_machine[rival]}')

            chosen_rival=int(input('Elige al pokemon de tu ribal que vas a atacar: '))-1

            c=list(attack_player.keys())
            team_machine[pokemons_player2[chosen_rival]]= team_machine[pokemons_player2[chosen_rival]] - (((team_machine[pokemons_player2[chosen_rival]])*(attack_player[c[0]]))/100)

            print(list(team_machine.values()))

            if 0 in list(team_machine.values()):
                eliminate=list(team_machine.values()).index(0)
                pokemons_player2.remove(eliminate)
            
        

        


        break

def game(object_pokemons):

    pokemones=['Pikachu','Caterpie','Pidgeotto','Bulbasaur','Charmander','Squirtle','Krabby','Raticate','Muk','Kingler']

    print("BIENVENIDO A BATALLA POKEMON:")
    num_players_str=input("Ingrese el numero de jugadores(1 o 2):")

    try:
        num_players=int(num_players_str)
    except:
        print('Ingrese un numero entero valido.')
    else:
        if num_players not in [1,2] :
            print('El numero de jugadores ingresados es incorrecto.')
            return
        
        player1_name,pokemons_player1,index_pokemons_player1=player(pokemones)
        pokemons_machine,index_pokemons_machine=machine(pokemones)

        print(f'los pokemones de {player1_name} son: {pokemons_player1} y sus indices son: {index_pokemons_player1}')

        battle(object_pokemons,index_pokemons_player1,pokemons_player1,pokemons_machine)

        if num_players == 2 :
            player2_name,pokemons_player2=player(pokemones)
        
        
        #print(f'los pokemones de la maquina son: {pokemons_machine}')

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
    print(object_pokemons[0].health)

    game(object_pokemons)

    #print(f"salud de pikachu: {pikachu.health}")
    #attack_name, damage_percentage = pikachu.perform_attack()
    #print(f"Ataque de pikachu y daño: {pikachu.perform_attack()}")


    for i in range(3):
        def selection_player():
            for i in range(len(pokemones)):
                if pokemones[i] not in pokemons_player:
                    print(f'{i+1}.{pokemones[i]}')    
            while True:
                choise_player=int(input('Escribe el numero del pokemon que deseas elegir: '))
                limpiar_consola()
                if choise_player in range(len(pokemones)):
                    break
                    
                else:
                    print('Opción no válida. Por favor, elige un Pokémon válido.')
                    time.sleep(1)
                    choise_player=selection_player()
                    break
            return choise_player