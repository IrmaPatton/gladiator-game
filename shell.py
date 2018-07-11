from core import *
from random import randint


def greet_rules():
    print('''                   Welcome to Gladiators: Rage Beasts 
It's a two player game, but if you want to play by yourself. I can't stop you
                   May the power of rage guide you''')


def make_player_1():
    Player1 = new_gladiator(100, 10, randint(10, 20), randint(21, 40))
    return Player1


def make_player_2():
    Player2 = new_gladiator(100, 10, randint(10, 20), randint(21, 40))
    return Player2
