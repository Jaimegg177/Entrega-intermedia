# -*- coding: utf-8 -*-
'''
Created on 24 nov. 2020

@author: jaime
'''

import csv
from collections import namedtuple
from numpy.core._multiarray_umath import conj
import statistics 

Team_Stats = namedtuple('Team_Stats', 'line, year, tm, team_name, wins, points, bigger_budget') 

##################################################################################################

def parse_bool(cadena):
    if cadena == 'True':
        booleano = True
    else:
        booleano = False
    return booleano

##################################################################################################
#Bloque 1

def lee_Team_stats_(fichero):
    with open(fichero, encoding='utf-8') as f:
        stats=[]
        lector=csv.reader(f)
        next(lector)
        for linea in lector:
            line=int(linea[0])
            year=int(linea[1])
            tm=linea[2]
            team_name=linea[3]
            wins=int(linea[4])
            points=float(linea[5])
            bigger_budget=parse_bool(linea[6])
            team=Team_Stats(line, year, tm, team_name, wins, points, bigger_budget)
            stats.append(team)
    return stats

'''
def lee_Team_stats(fichero):
    with open(fichero, encoding='utf-8') as f:
        lector = csv.reader(f)
        next(lector)
        result = [Team_stats(int(Line), int(Year), Tm, Team_Name, int(Wins), float(Points), parse_bool(Bigger_Budget)) for Line, Year, Tm, Team_Name, Wins, Points, Bigger_Budget in lector]
    return result
'''
##################################################################################################
#Bloque 2

def conjunto_equipos(team_stats):
    team_set=set(r.team_name for r in team_stats)
    return sorted(team_set)

def filtra_stats(team_stats, temporada):
    return [(r.team_name, r.points, r.year) for r in team_stats if r.year==temporada]

##################################################################################################
#Bloque 3

def promedio_stats(team_stats, temporada):
    filtered_by_year = filtra_stats(team_stats, temporada)
    point_list = list(r[1] for r in filtered_by_year)
    return sum(point_list) / len(point_list)
  
def calc_desviación_típica_por_año(team_stats, temporada):
    filtered_by_year = filtra_stats(team_stats, temporada)
    point_list = list(r[1] for r in filtered_by_year)
    dev=statistics.stdev(point_list)
    return dev

    ##############################################################################################
    #Bloque 4
    
    