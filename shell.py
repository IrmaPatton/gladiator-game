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


def player1_turn(Player1, Player2):
    #show player and stats and actions
    print('''

Gladiator: Blood Bath
Stats: -HP {}
       -Rage {}
       -Damage {} - {}
Actions: A - attack
         Y - attack youself
         H - heal
         P - pass turn
         Q - quit'''
          .format(Player1['health'], Player1['rage'], Player1['lowest damage'],
                  Player1['highest damage']))
    #does those actions
    action_input = input('What will Blood Bath do? ')
    if action_input == 'A':
        attack(Player1, Player2)
        print('HP = {} Rage = {}'.format(Player1['health'], Player1['rage']))
    elif action_input == 'Y':
        attack(Player1, Player1)
        print('HP = {} Rage = {}'.format(Player1['health'], Player1['rage']))
    elif action_input == 'H':
        heal(Player1)
        print('Blood Bath screamed in fury!')
        print('HP = {}'.format(Player1['health']))
    elif action_input == 'P':
        print('i not done yest')
    elif action_input == 'Q':
        print('Blood Bath throws down his weapon and rage quits.')
    else:
        print('''Actions: Type A to  attack
         Type H to heal
         Type P to pass turn
         Type Q to wimp out''')


def player2_turn(Player1, Player2):
    #show player and stats and actions
    print('''

Gladiator: Crazy Wolf
Stats: -HP {}
       -Rage {}
       -Damage {} - {}
Actions: A - attack
         Y - attack youself
         H - heal
         P - pass turn
         Q - quit'''
          .format(Player2['health'], Player2['rage'], Player2['lowest damage'],
                  Player2['highest damage']))
    #does those actions
    action_input = input('What will Crazy Wolf do? ')
    if action_input == 'A':
        attack(Player2, Player1)
        print('HP = {} Rage = {}'.format(Player2['health'], Player2['rage']))
    elif action_input == 'Y':
        attack(Player1, Player1)
        print('HP = {} Rage = {}'.format(Player1['health'], Player1['rage']))
    elif action_input == 'H':
        heal(Player2)
        print('Crazy Wolf snarled in fury!')
        print('HP = {}'.format(Player2['health']))
    elif action_input == 'P':
        print('i not done yest')
    elif action_input == 'Q':
        print('Crazy Wolf snaps at Blood Bath and rage quits.')
    else:
        print('''Actions: Type A to  attack
         Type H to heal
         Type P to pass turn
         Type Q to wimp out''')


def main():
    greet_rules()
    Player1 = make_player_1()
    Player2 = make_player_2()
    ready_set_go()
    player1_turn(Player1, Player2)


if __name__ == '__main__':
    main()
