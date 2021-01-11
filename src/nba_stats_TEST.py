# -*- coding: utf-8 -*-
'''
Created on 24 nov. 2020

@author: jaime
'''
from nba_stats import *
import nba_stats

#########################################################################################################
#Bloque 1

def test_lee_team_stats_(fichero):
    nba_stats = lee_Team_stats_(fichero) 
    print("Leídas" , len(nba_stats), "stats")
    print("Mostrando las 10 primeras\n")
    for i in range(10):
        print(nba_stats[i])
    return nba_stats

#########################################################################################################
#Bloque 2

def test_conjunto_equipos(fichero):
    print(conjunto_equipos(fichero))
    ''' 
     print("Mostrando los 10 primeros equipos")
     conjunto_equipos(fichero)
     for i in range (10):
         print(Team_Name)
    '''    
    
def test_filtra_stats(team_stats, paco):
    print(filtra_stats(team_stats, paco))

#########################################################################################################
#Bloque 3

def test_promedio_stats(team_stats, temporada):
    print(promedio_stats(team_stats, temporada))
    
def test_calc_desviación_típica_por_año(team_stats, temporada):
    print(calc_desviación_típica_por_año(team_stats, temporada))
    
#########################################################################################################

if __name__ == '__main__':
    # Generamos la colección principal de datos desde el csv.
    nba_stats = test_lee_team_stats_('../data/Team_stats_.csv')
    test_conjunto_equipos(nba_stats)
    
    # Se solicita al usuario que untroduzca un año para obtener los datos y comprobamos que introduce un valor válido
    year = int(input("¿De qué año quiere ver los registros? (1969-2019)"))
    while not (year > 1968 and year < 2020):
        print("Lo siento, el dato no es válido")
        year = int(input("¿De qué año quiere ver los registros? (1969-2019)"))

    # Se usa el año introducido por el usuario para que se filtre la colección nba_stats y para calcular el promedio de puntos de esa temporada (año)
    test_filtra_stats(nba_stats, year)
    print("El promedio de puntos de este año fue: ")
    test_promedio_stats(nba_stats, year)
    
    init_year = int(input("¿Desde qué año quiere saber la desviación tipica? El más antiguo es 1967"))
    limit_year = int(input("¿Desde qué año quiere saber la desviación tipica? El más reciente es 2019"))
    
    while not (init_year < limit_year or init_year<1967 or limit_year>2019):
        print("Lo siento, el dato no es válido. El año inicial debe ser inferior al final y debe respetar los límites. Por favor elija de nuevo.")
        init_year = int(input("¿Desde qué año quiere saber la desviación estándar? El más antiguo es 1967"))
        limit_year = int(input("¿Desde qué año quiere saber la desviación estándar? El más reciente es 2019"))

    # La desviación típica aplicada al conjunto de datos para un año, nos permite conocer cómo de ajustada estuvo la liga para el año elegido
    # Lo calculamos para cada año del intervalo solicitado
    i = init_year
    while i < limit_year:
        print("El año ", i)
        test_calc_desviación_típica_por_año(nba_stats, i)
        i += 1

