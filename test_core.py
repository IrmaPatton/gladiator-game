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
