from random import randint


def new_gladiator(health, rage, damage_low, damage_high):
    '''input -> dictionary
    Returns a dictionary representing the gladiator with 
    the provided values: health, rage, lowest damage, and highest damage'''

    gladiator = {
        'health': health,
        'rage': rage,
        'lowest damage': damage_low,
        'highest damage': damage_high
    }
    return gladiator


def attack(attacker, defender):
    '''dictionary -> None
    Attacker(gladiator) strikes  defender(other gladiator)
    with normal hit or critical hit, and gladiators reacts accordingly'''

    hit = randint(attacker['lowest damage'], attacker['highest damage'])
    # randomly generates a number between 1 and 99
    probability = randint(1, 99)
    if probability <= attacker['rage']:  # if a critical hit
        health = defender['health'] - (2 * hit)
        # makes sure health does not drop below 0
        defender['health'] = max(health, 0)
        attacker['rage'] = 0
    else:
        health = defender['health'] - hit
        # makes sure health does not drop below 0
        defender['health'] = max(health, 0)
        rage = attacker['rage'] + 15
        # makes sure rage does not go over 100
        attacker['rage'] = min(rage, 100)


def heal(gladiator):
    '''dictionary -> bool or None
    Makes gladiator use rage to heal 5 HP'''

    #make sure gladiator's health stays less then 100
    if gladiator['health'] >= 100:
        gladiator['health'] = min(gladiator['health'], 100)
    #make sure gladiator can heal
    elif gladiator['rage'] < 10:
        return None
    #gladiator uses the Power of Rage! to heal
    else:
        gladiator['rage'] = gladiator['rage'] - 10
        gladiator['health'] = gladiator['health'] + 5


def is_dead(gladiator):
    '''dictionary -> bool
    Checks gladiator's health and if they are dead returns True or False'''

    if gladiator['health'] == 0:
        return True
    else:
        return False
