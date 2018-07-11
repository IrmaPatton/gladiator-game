from core import *
from random import randint


def greet_rules():
    print('''                   Welcome to Gladiators: Rage Beasts 
It's a two player game, but if you want to play by yourself. I can't stop you
                   May the power of rage guide you''')


def make_player_1():
    low_damage = randint(10, 20)
    high_damage = randint(21, 40)
    Player1 = new_gladiator(100, 10, low_damage, high_damage)
    return Player1


def make_player_2():
    Player2 = new_gladiator(100, 10, randint(10, 20), randint(21, 40))
    return Player2


def ready_set_go():
    print('''

Ready...Set... BATTLE!!!!''')


def battle_time(Player1, Player2):
    #show players and stats and actions
    print('''

Gladiator: Blood Bath
Stats: -HP {}
       -Rage {}
       -Damage {} - {}
Actions: A - attack
         H - heal
         P - pass turn
         Q - quit'''
          .format(Player1['health'], Player1['rage'], Player1['lowest damage'],
                  Player1['highest damage']))
    #does those actions
    action_input = input('What will Blood Bath do? ')
    while True:
        if action_input == 'A':
            attack(Player1, Player2)
            print('HP = {} Rage = {}'.format(Player1['health'],
                                             Player1['rage']))
            break


def main():
    greet_rules()
    Player1 = make_player_1()
    Player2 = make_player_2()
    ready_set_go()
    battle_time(Player1, Player2)


if __name__ == '__main__':
    main()
