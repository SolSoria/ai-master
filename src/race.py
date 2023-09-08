# funcion para obtener la raza de una persona basado en su comportamiento de compra

Suggestion 1

def getRace():
    # se obtiene un numero aleatorio
    random = randint(0, 100)
    # se comprueba si el numero aleatorio esta en el rango de la raza
    if random <= 40:
        return 'white'
    elif random <= 70:
        return 'black'
    elif random <= 85:
        return 'asian'
    elif random <= 95:
        return 'hispanic'
    else:
        return 'other'

=======
Suggestion 2

def getRace(buyer):
    if buyer == 'Cautious' or buyer == 'Impulsive' or buyer == 'Average':
        return 'White'
    elif buyer == 'Careful' or buyer == 'Demanding' or buyer == 'Rational':
        return 'Black'
    elif buyer == 'Spontaneous' or buyer == 'Compulsive' or buyer == 'Hasty':
        return 'Asian'
    elif buyer == 'Loyal' or buyer == 'Sensible' or buyer == 'Observant':
        return 'Hispanic'
    else:
        return 'Other'
