from core import *


def test_new_gladiator():
    gladiator = new_gladiator(100, 10, 23, 46)
    assert gladiator == {'health': 100, 'rage': 10, 'lowest damage': 23}
