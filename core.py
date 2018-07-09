def new_gladiator(health, rage, damage_low, damage_high):
    '''input -> dictionary
    Returns a dictionary representing the gladiator
    with the provided values.'''
    gladiator = {
        'health': health,
        'rage': rage,
        'lowest damage': damage_low,
        'highest damage': damage_high
    }
    return gladiator
