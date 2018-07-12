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


def input_action():
    #function to input, checks it and returns input
    while True:
        action = input('What will he do? ')
        if action == 'A':
            return action
        elif action == 'Y':
            return action
        elif action == 'H':
            return action
        elif action == 'P':
            return action
        elif action == 'Q':
            return action
        else:
            print('''
Actions: Type A to  attack
         Type Y to build rage in unhealthy way
         Type H to heal
         Type P to pass turn
         Type Q to wimp out''')


def Y_check_P1(Player1):
    #checks if Blood Bath killed himself
    if is_dead(Player1) == True:
        print("""Blood Bath's unhealthy rage seeking was his end.
Crazy Wolf bows his head in admiration of Blood Bath's commitment to be a Rage Beast."""
              )
        exit()
    else:
        return None


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
    action_input = input_action()
    if action_input == 'A':
        attack(Player1, Player2)
        print('HP = {} Rage = {}'.format(Player1['health'], Player1['rage']))
    elif action_input == 'Y':
        attack(Player1, Player1)
        Y_check_P1(Player1)
        print('HP = {} Rage = {}'.format(Player1['health'], Player1['rage']))
    elif action_input == 'H':
        heal(Player1)
        print('Blood Bath screamed in fury!')
        print('HP = {}'.format(Player1['health']))
    elif action_input == 'P':
        return None
    elif action_input == 'Q':
        print('Blood Bath throws down his weapon and rage quits.')
        exit()


def Y_check_P2(Player2):
    #checks if Crazy Wolf killed himself
    if is_dead(Player2) == True:
        print('''Crazy Wolf's unhealthy rage seeking was his downfall.
Blood Bath bows his head in admiration of Blood Bath's commitment to be a Rage Wolf.'''
              )
    else:
        return None


def player2_turn(Player2, Player1):
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
    action_input = input_action()
    if action_input == 'A':
        attack(Player2, Player1)
        print('HP = {} Rage = {}'.format(Player2['health'], Player2['rage']))
    elif action_input == 'Y':
        attack(Player2, Player2)
        Y_check_P2(Player2)
        print('HP = {} Rage = {}'.format(Player2['health'], Player2['rage']))
    elif action_input == 'H':
        heal(Player2)
        print('Crazy Wolf snarled in fury!')
        print('HP = {}'.format(Player2['health']))
    elif action_input == 'P':
        return None
    elif action_input == 'Q':
        print('Crazy Wolf snaps at Blood Bath and rage quits.')
        exit()


def main():
    greet_rules()
    Player1 = make_player_1()
    Player2 = make_player_2()
    ready_set_go()
    while True:
        if is_dead(Player1) == True:
            #i think the new statements is boring compared
            print("Crazy Wolf has the victory, the crowd chant his name")
            break
        player1_turn(Player1, Player2)
        if is_dead(Player2) == True:
            #had to tone down the wining statements to something... less edgy
            print("Blood Bath has the victory,the crowd chants his name.")
            break
        player2_turn(Player2, Player1)


if __name__ == '__main__':
    main()
