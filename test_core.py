from core import *


def test_new_gladiator():

    assert new_gladiator(100, 10, 23, 46) == {
        'health': 100,
        'rage': 10,
        'lowest damage': 23,
        'highest damage': 46
    }
    assert new_gladiator(0, 0, 0, 0) == {
        'health': 0,
        'rage': 0,
        'lowest damage': 0,
        'highest damage': 0
    }


def test_attack():
    #to test if normal hit is good
    random_gladiator = {
        'health': 100,
        'rage': 0,
        'lowest damage': 23,
        'highest damage': 23
    }
    Bob_gladiator = {
        'health': 100,
        'rage': 0,
        'lowest damage': 13,
        'highest damage': 13
    }

    attack(Bob_gladiator, random_gladiator)

    assert random_gladiator['health'] == 87
    assert Bob_gladiator['rage'] == 15


def test_attack():
    #test if critical hit is good
    random_gladiator = {
        'health': 100,
        'rage': 0,
        'lowest damage': 23,
        'highest damage': 23
    }
    Bob_gladiator = {
        'health': 100,
        'rage': 99,
        'lowest damage': 13,
        'highest damage': 13
    }

    attack(Bob_gladiator, random_gladiator)

    assert random_gladiator['health'] == 74
    assert Bob_gladiator['rage'] == 0


def heal():
    #tests if gladiator can heal normally
    Bob_gladiator = {
        'health': 1,
        'rage': 10,
        'lowest damage': 13,
        'highest damage': 13
    }

    heal(Bob_gladiator)

    assert Bob_gladiator['health'] == 6
    assert Bob_gladiator['rage'] == 0


def heal():
    #test when gladiator can't heal
    Bob_gladiator = {
        'health': 1,
        'rage': 9,
        'lowest damage': 13,
        'highest damage': 13
    }

    heal(Bob_gladiator)

    assert Bob_gladiator['health'] == 1
