# funcion para determinar la religion de una persona por su nombre

=======
Suggestion 1

def get_religion(name):
    religion = ''
    if name == 'Juan':
        religion = 'catolico'
    elif name == 'Pedro':
        religion = 'catolico'
    elif name == 'Maria':
        religion = 'catolico'
    elif name == 'Jose':
        religion = 'catolico'
    elif name == 'Luis':
        religion = 'catolico'
    elif name == 'Ana':
        religion = 'catolico'

    return religion

=======
Suggestion 2

def test_religion():
    # se crea una lista de nombres
    names = [
        {'name': 'Juan', 'religion': 'catolico'},
        {'name': 'Pedro', 'religion': 'catolico'},
        {'name': 'Maria', 'religion': 'catolico'},
        {'name': 'Jose', 'religion': 'catolico'},
        {'name': 'Luis', 'religion': 'catolico'},
        {'name': 'Ana', 'religion': 'catolico'},
    ]

    # se crea una instancia de la clase Religion
    religion = Religion(names)
    # se llama al metodo get_religion
    religion = religion.get_religion()
    # se valida el resultado
    assert religion == {'name': 'Jose', 'religion': 'catolico'}

=======
Suggestion 3

def get_religion(name):
    if name == 'Juan':
        return 'catolico'
    elif name == 'Pedro':
        return 'catolico'
    elif name == 'Maria':
        return 'catolico'
    elif name == 'Jose':
        return 'catolico'
    elif name == 'Luis':
        return 'catolico'
    elif name == 'Ana':
        return 'catolico'
    elif name == 'Raul':
        return 'catolico'
    elif name == 'Miguel':
        return 'catolico'
    elif name == 'Gabriela':
        return 'catolico'
    elif name == 'Rosa':
        return 'catolico'
    elif name == 'Francisco':
        return 'catolico'
    elif name == 'Guadalupe':
        return 'catolico'
    elif name == 'Alejandro':
        return 'catolico'
    elif name == 'Javier':
        return 'catolico'
    elif name == 'Fernando':
        return 'catolico'
    elif name == 'Julio':
        return 'catolico'
    elif name == 'Ricardo':
        return 'catolico'
    elif name == 'Eduardo':
        return 'catolico'
    elif name == 'Diana':
        return 'catolico'
    elif name == 'Claudia':
        return 'catolico'
    elif name == 'Mariana':
        return 'catolico'
    elif name == 'Andrea':
        return 'catolico'
    elif name == 'Jorge':
        return 'catolico'
    elif name == 'Sofia':
        return 'catolico'
    elif name == 'Sergio':
        return 'catolico'
    elif name == 'Roberto':
        return 'catolico'
    elif name == 'Samantha':
        return 'catolico'
    elif name == 'Luisa':
        return 'catolico'
    elif name == 'Fernanda':
        return 'catolico'
    elif name == 'Carlos':
        return 'catolico'
    elif name == 'Rafael':
        return 'catolico'
    elif name == 'Mauricio':
        return 'catolico'
    elif name

=======
Suggestion 4

def get_religion(name):
    if name in ['Juan', 'Pedro', 'Maria', 'Jose', 'Luis', 'Ana']:
        return 'catolica'
    elif name in ['David', 'Daniel', 'Alejandro', 'Cristian', 'Javier', 'Diego']:
        return 'cristiana'
    elif name in ['Ricardo', 'Raul', 'Roberto', 'Rodrigo', 'Ramon', 'Rafael']:
        return 'judia'
    elif name in ['Miguel', 'Mauricio', 'Martin', 'Mateo', 'Marcos', 'Manuel']:
        return 'budista'
    else:
        return 'otra'

=======
Suggestion 5

def get_religion(name):
    # se crea un diccionario con los nombres de las religiones
    religions = {
        'juan': 'catolica',
        'pedro': 'catolica',
        'maria': 'catolica',
        'jose': 'catolica',
        'luis': 'catolica',
        'ana': 'catolica',
        'lucia': 'catolica',
        'laura': 'catolica',
        'pablo': 'catolica',
        'david': 'catolica',
        'alejandro': 'catolica',
        'camilo': 'catolica',
        'sebastian': 'catolica',
        'carlos': 'catolica',
        'andres': 'catolica',
        'julian': 'catolica',
        'santiago': 'catolica',
        'emilio': 'catolica',
        'jorge': 'catolica',
        'javier': 'catolica',
        'miguel': 'catolica',
        'daniel': 'catolica',
        'francisco': 'catolica',
        'manuel': 'catolica',
        'rafael': 'catolica',
        'fernando': 'catolica',
        'jose': 'catolica',
        'ramon': 'catolica',
        'eduardo': 'catolica',
        'alberto': 'catolica',
        'diego': 'catolica',
        'enrique': 'catolica',
        'julio': 'catolica',
        'antonio': 'catolica',
        'jose': 'catolica',
        'ignacio': 'catolica',
        'victor': 'catolica',
        'ruben': 'catolica',
        'sergio': 'catolica',
        'oscar': 'catolica',
        'roberto': 'catolica',
        'carlos': 'catolica',
        'jaime': 'catolica',
        'jose': 'catolica',
        'adrian': 'catolica',
        'arturo': 'catolica',
        'gabriel': '

=======
Suggestion 6

def test_get_religion():
    # se crea una lista de nombres
    names = [
        {'name': 'Juan'},
        {'name': 'Pedro'},
        {'name': 'Maria'},
        {'name': 'Jose'},
        {'name': 'Luis'},
        {'name': 'Ana'},
    ]

    # se crea una lista de religiones
    religions = [
        {'name': 'Juan', 'religion': 'catolica'},
        {'name': 'Pedro', 'religion': 'catolica'},
        {'name': 'Maria', 'religion': 'catolica'},
        {'name': 'Jose', 'religion': 'catolica'},
        {'name': 'Luis', 'religion': 'catolica'},
        {'name': 'Ana', 'religion': 'catolica'},
    ]

    # se crea una instancia de la clase Religion
    religion = Religion(names, religions)
    # se llama al metodo get_religion
    religion = religion.get_religion()
    # se valida el resultado
    assert religion == {'name': 'Jose', 'religion': 'catolica'}

=======
Suggestion 7

def get_religion_by_name(name):
    # se crea un diccionario con los nombres y sus religiones
    religions = {
        'jose': 'catolico',
        'maria': 'catolico',
        'pedro': 'catolico',
        'juan': 'catolico',
        'sofia': 'catolico',
        'luis': 'catolico',
        'carlos': 'catolico',
        'david': 'catolico',
        'andres': 'catolico',
        'laura': 'catolico',
        'javier': 'catolico',
        'camilo': 'catolico',
        'juanita': 'catolico',
        'juliana': 'catolico',
        'pablo': 'catolico',
        'sebastian': 'catolico',
        'alejandro': 'catolico',
        'jorge': 'catolico',
        'daniel': 'catolico',
        'jimena': 'catolico',
        'andrea': 'catolico',
        'santiago': 'catolico',
        'carolina': 'catolico',
        'natalia': 'catolico',
        'mateo': 'catolico',
        'cristian': 'catolico',
        'miguel': 'catolico',
        'mario': 'catolico',
        'julian': 'catolico',
        'jessica': 'catolico',
        'juan': 'catolico',
        'oscar': 'catolico',
        'johana': 'catolico',
        'daniela': 'catolico',
        'adriana': 'catolico',
        'alejandra': 'catolico',
        'cristina': 'catolico',
        'monica': 'catolico',
        'luisa': 'catolico',
        'fabiola': 'catolico',
        'diana': 'catolico',
        'julio': 'catolico',
        'lina': 'catolico',
        'fernando': 'catolico',
        'lucia': 'catolico',
        'carla': 'catolico

=======
Suggestion 8

def test_get_religion():
    # se crea una lista de personas
    people = [
        {'name': 'Juan', 'religion': 'catolica'},
        {'name': 'Pedro', 'religion': 'catolica'},
        {'name': 'Maria', 'religion': 'catolica'},
        {'name': 'Jose', 'religion': 'catolica'},
        {'name': 'Luis', 'religion': 'catolica'},
        {'name': 'Ana', 'religion': 'catolica'},
    ]

    # se crea una instancia de la clase Religion
    religion = Religion(people)
    # se llama al metodo get_best_candidate
    religion = religion.get_religion()
    # se valida el resultado
    assert religion == 'catolica'
