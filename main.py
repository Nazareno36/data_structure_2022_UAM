'''
    Author: Carlos Páez
    Vers: 1.0
    Language: Python
'''

# def say_hello():
#     print('Hello World')

# say_hello()

# def input_data_user():
#     user_name = input('Ingresa tu nombre: ')
#     #se debe validar que el valor ingresado sea un numero
#     while True:
#         try:
#             age = int(input('Ingrese la edad: '))
#             break
#         except:
#             print('El valor ingresado no es valido')
#     print(f'{user_name} tiene {age} años.')

# input_data_user()

# def input_frameworks_data():
#     while True:
#         try:
#             languages_count = int(input('Cuantos fm conoces? -> '))
#             counter = 1
#             while counter <= languages_count:
#                 framework_name = input('Framework -> ')
#                 counter+=1
#             break
#         except:
#             print('El valor ingresado no es valido')

# input_frameworks_data()

# def input_language_information():
#     #Declaracion de una lista vacía
#     language_list = []
#     while True:
#         try:
#             language_count = int(input('Cuantos lenguajes de programacion conoces? -> '))
#             for item_language in range(language_count):
#                 language_name = input(f'{item_language + 1} : ')
#                 language_list.append(language_name)
#             break
#         except:
#             print('El valor ingresado no es valido')
#     print(language_list)

# input_language_information()

# def insert_info_student():
#     #Solicitar nombre y documento del estudiante
#     print('Ingresa la siguiente informacion')
#     students_list = []
#     while True:
#         try:
#             student_counter = int(input('Cuantos estudiantes ingresa -> '))
#             for item_student in range(1, student_counter+1):
#                 student_name = input('Nombre: ')
#                 student_document = input('Documento: ')
#                 students_list.append((item_student,student_name,student_document))
#             print(f'Los estudiantes que ingresaste, son:\n{students_list}')
#             break
#         except:
#             print('El valor ingresado no es valido')

def countries_information():
    countries_list = []
    while True:
        try:
            countries = int(input('Cuantos paises conoce? -> '))
            for item_country in range(1,countries+1):
                country_name = input('Pais: ')
                while True:
                    try:
                        population = int(input('Poblacion: '))
                        break
                    except:
                        print('El valor ingresado no es valido')
                countries_list.append((country_name, population))
            print(f'Los paises son: \n{countries_list}')
        except:
            print('El valor ingresado no es valido')
        break
                    