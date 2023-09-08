# funcion para determinar si un candidato es el mejor para una vacante

=======
Suggestion 1

def test_best_candidate():
    # se crea una vacante
    vacante = Vacante.objects.create(
        nombre='Vacante de prueba',
        descripcion='Esta es una vacante de prueba',
        salario=10000
    )
    # se crean 3 candidatos
    candidato1 = Candidato.objects.create(
        nombre='Candidato 1',
        apellido='Apellido 1',

=======
Suggestion 2

# return: booleano

=======
Suggestion 3

def test_best_candidate():
    # se crea una lista de candidatos
    candidates = [
        {'name': 'Juan', 'age': 32, 'skills': ['python', 'java', 'php']},
        {'name': 'Pedro', 'age': 25, 'skills': ['python', 'java']},
        {'name': 'Maria', 'age': 27, 'skills': ['python', 'php']},
        {'name': 'Jose', 'age': 28, 'skills': ['python', 'java', 'php']},
        {'name': 'Luis', 'age': 30, 'skills': ['python', 'java', 'php']},
        {'name': 'Ana', 'age': 27, 'skills': ['python', 'java']},
    ]

    # se crea una lista de vacantes
    vacancies = [
        {'name': 'Developer Python', 'skills': ['python', 'java', 'php']},
        {'name': 'Developer Java', 'skills': ['python', 'java']},
        {'name': 'Developer PHP', 'skills': ['python', 'php']},
    ]

    # se crea una instancia de la clase BestCandidate
    best_candidate = BestCandidate(candidates, vacancies)
    # se llama al metodo get_best_candidate
    best_candidate = best_candidate.get_best_candidate()
    # se valida el resultado
    assert best_candidate == {'name': 'Jose', 'age': 28, 'skills': ['python', 'java', 'php']}

=======
Suggestion 4

# 
# @param: id de la vacante, id del candidato
# @return: booleano

=======
Suggestion 5

# @param: id_candidato, id_vacante
# @return: booleano

=======
Suggestion 6

def test_candidato_vacante():
    assert candidato_vacante(10, 10, 10) == True
    assert candidato_vacante(10, 10, 9) == True
    assert candidato_vacante(10, 10, 11) == False
    assert candidato_vacante(10, 11, 10) == False
    assert candidato_vacante(11, 10, 10) == False
    assert candidato_vacante(10, 9, 10) == True
    assert candidato_vacante(11, 9, 10) == False
    assert candidato_vacante(10, 9, 11) == False
    assert candidato_vacante(9, 10, 10) == False
    assert candidato_vacante(9, 11, 10) == False
    assert candidato_vacante(9, 10, 11) == False
    assert candidato_vacante(9, 9, 9) == True
    assert candidato_vacante(9, 9, 10) == True
    assert candidato_vacante(9, 10, 9) == True
    assert candidato_vacante(10, 9, 9) == True
    assert candidato_vacante(9, 11, 9) == False
    assert candidato_vacante(9, 9, 11) == False
    assert candidato_vacante(11, 9, 9) == False
    assert candidato_vacante(11, 11, 11) == False
    assert candidato_vacante(11, 11, 10) == False
    assert candidato_vacante(11, 10, 11) == False
    assert candidato_vacante(10, 11, 11) == False
    assert candidato_vacante(11, 10, 10) == False
    assert candidato_vacante(10, 11, 10) == False
    assert candidato_vacante(10, 10, 11) == False
    assert candidato_vacante(11, 11, 9

=======
Suggestion 7

def test_candidato():
    candidatos = [
        {'nombre': 'Juan', 'edad': 26, 'experiencia': 1, 'tecnologias': ['python', 'django', 'flask', 'c#']},
        {'nombre': 'Pedro', 'edad': 26, 'experiencia': 3, 'tecnologias': ['java', 'spring', 'c#', 'ruby']},
        {'nombre': 'Maria', 'edad': 26, 'experiencia': 2, 'tecnologias': ['python', 'django', 'flask', 'c#']},
        {'nombre': 'Luis', 'edad': 26, 'experiencia': 1, 'tecnologias': ['python', 'django', 'flask', 'c#']},
        {'nombre': 'Jorge', 'edad': 26, 'experiencia': 3, 'tecnologias': ['java', 'spring', 'c#', 'ruby']},
    ]

    vacante = {
        'tecnologias': ['python', 'django', 'flask'],
        'experiencia': 2
    }

    mejor_candidato = None
    for candidato in candidatos:
        if candidato['experiencia'] >= vacante['experiencia']:
            for tecnologia in vacante['tecnologias']:
                if tecnologia not in candidato['tecnologias']:
                    break
            else:
                if mejor_candidato is None:
                    mejor_candidato = candidato
                else:
                    if candidato['experiencia'] > mejor_candidato['experiencia']:
                        mejor_candidato = candidato

    print(mejor_candidato)

=======
Suggestion 8

def test_best_candidate():
    # se crea un objeto de la clase Vacancy
    vacancy = Vacancy()
    # se crea un objeto de la clase Candidate
    candidate = Candidate()
    # se crea un objeto de la clase Candidate
    candidate2 = Candidate()
    # se crea un objeto de la clase Candidate
    candidate3 = Candidate()
    # se crea un objeto de la clase Candidate
    candidate4 = Candidate()
    # se crea un objeto de la clase Candidate
    candidate5 = Candidate()
    # se crea un objeto de la clase Candidate
    candidate6 = Candidate()
    # se crea un objeto de la clase Candidate
    candidate7 = Candidate()
    # se crea un objeto de la clase Candidate
    candidate8 = Candidate()
    # se crea un objeto de la clase Candidate
    candidate9 = Candidate()
    # se crea un objeto de la clase Candidate
    candidate10 = Candidate()
    # se crea un objeto de la clase Candidate
    candidate11 = Candidate()
    # se crea un objeto de la clase Candidate
    candidate12 = Candidate()
    # se crea un objeto de la clase Candidate
    candidate13 = Candidate()
    # se crea un objeto de la clase Candidate
    candidate14 = Candidate()
    # se crea un objeto de la clase Candidate
    candidate15 = Candidate()
    # se crea un objeto de la clase Candidate
    candidate16 = Candidate()
    # se crea un objeto de la clase Candidate
    candidate17 = Candidate()
    # se crea un objeto de la clase Candidate
    candidate18 = Candidate()
    # se crea un objeto de la clase Candidate
    candidate19 = Candidate()
    # se crea un objeto de la clase Candidate
    candidate20 = Candidate()
    # se crea un objeto de la clase Candidate
    candidate21 = Candidate()
    # se crea un objeto de la clase Candidate
    candidate22 = Candidate()
    # se crea un objeto de la clase Candidate
    candidate23 = Candidate()
    # se crea un objeto de la clase Candidate
    candidate24 = Candidate()
    # se crea un objeto de la clase Candidate
    candidate25 = Candidate()
    # se crea un objeto de la clase Candidate
    candidate26 = Candidate()
    # se crea un objeto de la clase Candidate
    candidate27 = Candidate()
    # se crea un objeto de la clase Candidate
    candidate28 = Candidate()

=======
Suggestion 9

# Entrada: candidatos, lista de candidatos
#          vacante, vacante a la que se le quiere encontrar el mejor candidato
# Salida: candidato, candidato que mejor se ajusta a la vacante


## la mejor opcion
def test_candidato():
    candidatos = [
        {'nombre': 'Juan', 'edad': 26, 'experiencia': 1, 'tecnologias': ['python', 'django', 'flask', 'c#']},
        {'nombre': 'Pedro', 'edad': 26, 'experiencia': 3, 'tecnologias': ['java', 'spring', 'c#', 'ruby']},
        {'nombre': 'Maria', 'edad': 26, 'experiencia': 2, 'tecnologias': ['python', 'django', 'flask', 'c#']},
        {'nombre': 'Luis', 'edad': 26, 'experiencia': 1, 'tecnologias': ['python', 'django', 'flask', 'c#']},
        {'nombre': 'Jorge', 'edad': 26, 'experiencia': 3, 'tecnologias': ['java', 'spring', 'c#', 'ruby']},
    ]

    vacante = {
        'tecnologias': ['python', 'django', 'flask'],
        'experiencia': 2
    }

    mejor_candidato = None
    for candidato in candidatos:
        if candidato['experiencia'] >= vacante['experiencia']:
            for tecnologia in vacante['tecnologias']:
                if tecnologia not in candidato['tecnologias']:
                    break
            else:
                if mejor_candidato is None:
                    mejor_candidato = candidato
                else:
                    if candidato['experiencia'] > mejor_candidato['experiencia']:
                        mejor_candidato = candidato

    print(mejor_candidato)