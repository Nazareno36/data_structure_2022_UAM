import sys


class Activity1:

    #Constructor de la clase
    def __init__(self) -> None:
        self.editor_name = 'Visual Studio Code'
        self.language = 'Python'
        self.version = 3.0
        self.user_name
        self.frameworks_list = []
        self.language_list = []
        self.students_list = []
        self.countries_list = []
    
    def show_info(self):
        print(f'Estamos trabajando en {self.editor_name}\nprogramando en {self.language} {self.version}')

    def say_hello():
        print('Hello World')

    def input_data_user(self):
        self.user_name = input('Ingresa tu nombre: ')
        #se debe validar que el valor ingresado sea un numero
        while True:
            try:
                age = int(input('Ingrese la edad: '))
                break
            except:
                print('El valor ingresado no es valido')
        print(f'{self.user_name} tiene {age} años.')

    def input_frameworks_data(self):
        while True:
            try:
                languages_count = int(input('Cuantos fm conoces? -> '))
                counter = 1
                while counter <= languages_count:
                    framework_name = input('Framework -> ')
                    self.frameworks_list.append(framework_name)
                    counter+=1
                break
            except:
                print('El valor ingresado no es valido')
        print(self.frameworks_list)

    def input_language_information(self):
        #Declaracion de una lista vacía
        while True:
            try:
                language_count = int(input('Cuantos lenguajes de programacion conoces? -> '))
                for item_language in range(language_count):
                    language_name = input(f'{item_language + 1} : ')
                    self.language_list.append(language_name)
                break
            except:
                print('El valor ingresado no es valido')
        print(self.language_list)

    def insert_info_student(self):
        #Solicitar nombre y documento del estudiante
        print('Ingresa la siguiente informacion')
        while True:
            try:
                student_counter = int(input('Cuantos estudiantes ingresa -> '))
                for item_student in range(1, student_counter+1):
                    student_name = input('Nombre: ')
                    student_document = input('Documento: ')
                    self.students_list.append((item_student,student_name,student_document))
                print(f'Los estudiantes que ingresaste, son:\n{self.students_list}')
                break
            except:
                print('El valor ingresado no es valido')

    def countries_information(self):
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
                    self.countries_list.append((country_name, population))
                print(f'Los paises son: \n{self.countries_list}')
            except:
                print('El valor ingresado no es valido')
            break
        print(self.countries_list)

    def bigger_population(self):
        b_population = -1
        counter = 0
        pos = 0
        for item in self.countries_list:
            if item[1] > b_population:
                b_population = item[1]
                pos =  counter
            counter+=1
        return self.countries_list[pos][0]

    def smallest_population(self):
        s_population = sys.maxsize
        counter = 0
        pos = 0
        for item in self.countries_list:
            if item[1] < s_population:
                s_population = item[1]
                pos =  counter
            counter+=1
        return self.countries_list[pos][0]