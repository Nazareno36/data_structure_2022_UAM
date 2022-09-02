'''
    Author: Carlos Páez
    Vers: 1.0
    Language: Python
'''
#Desde el archivo importamos la clase
from activity1 import Activity1

instance = Activity1()

countries_list = [('Medallo',102),('Bogota',20),('JesusTeAma',101)]
n = instance.bigger_population(countries_list)
print(n)    

