from math import *
import numpy as np

def ackley(x):
    return -exp(-sqrt(0.5*sum([i**2 for i in x]))) - exp(0.5*sum([cos(i) for i in x])) + 1 + exp(1)

def bukin(x):
    return 100*sqrt(abs(x[1]-0.01*x[0]**2)) + 0.01*abs(x[0] + 10)

def bohachevsky(x):
    return x[0]**2 + 2*x[1]**2 - 0.3*cos(3*pi*x[0]) - 0.4*cos(4*pi*x[1]) + 0.7

def sum_squares_function(x):
    return sum([(i+1)*x[i]**2 for i in range(len(x))])

def room(x):
    # global pos
    pos = x
    #print("pos", pos)
    #[1,1,2,2,3,3,4,4,5,5,6,6,7,7,8,8,9,9,10,10] - srodki tych mebli, wymiary oznaczaja odleglosc miedzy srodkiem a koncem
    #telewiyor, lawa, pufa1, pufa2, kanapa, fotel, szafka1, szafka2, szafka3, szafka4
    mes = [0.7,0.2, 0.50,0.30, 0.25,0.25, 0.25,0.25, 0.70,0.40, 0.45,0.40, 0.30,0.20, 0.70,0.20, 0.20,0.20, 0.45,0.20]
    on_carpet = [0,0, 1,1 ,1,1 ,1,1, 0,0, 1,1, 0,0 ,0,0, 0,0, 0,0]
    window = [0,2]
    door = [3,0]

    carpet_size = 0
    r = find_smallest_r(pos, on_carpet, mes, window, door)

    carpet_size = pi*r*r
    #print("carpet size: ", carpet_size)
    return -carpet_size

def find_smallest_r(pos, on_car, mes, win, doo):
    r = 4
    if is_out_of_room(pos, mes):
        return 0
        # nachodzenie na siebie
    # if is_overlapping(pos, mes):
    #     return 0
    elif is_door_or_window_blocked(pos,mes):
        return 0
    else:
        r = get_min_dist(pos, mes)
    return r

def is_door_or_window_blocked(pos, mes):
    #zakladamy ze szer okna to 60x2 a drzwi 45x2, a zasloniecie to postawienie w mniejszej odl niz ich szer
    for i in range(0, 20, 2):
        if (pos[i]-0.5*mes[i] < 3.45 and pos[i]+0.5*mes[i] > 2.55 and pos[i+1]-mes[i+1] < 0.45):
            return True
    for i in range(1, 19, 2):
        if (pos[i]-0.5*mes[i] < 2.6 and pos[i]+0.5*mes[i] > 1.4 and pos[i+1]-mes[i+1] < 0.6):
            return True
    return False

def get_min_dist(pos, mes):
    arr = []
    for i in [0,8,12,14,16,18]:
        arr.append(get_distance(pos[i]+0.5*mes[i],pos[i]-0.5*mes[i],pos[i+1]-0.5*mes[i+1],pos[i+1]+0.5*mes[i+1]))
    return min(arr)

def get_distance(xmax,xmin, ymin, ymax):
    dx = max(xmin-2, 2-xmax)
    dy = max(ymin - 2, 2 - ymax)
    return sqrt(dx*dx+dy*dy)

def is_out_of_room(pos, mes):
    for i in range(len(pos)):
        # wykluczenie przypadkow ze wychodzi poza pokoj
        if 0.5*mes[i]>pos[i]:
            return True
    return False

def is_overlapping(pos, mes):
    temp = False
    for l in range(len(pos)-2):
        # dla y
        if l %2 != 0:
            for j in range(l+2,len(pos),2):
                if (pos[l] - 0.5*mes[l] < pos[j] + 0.5*mes[j] and pos[l] + 0.5*mes[l] >= pos[j] - 0.5*mes[j]) or (pos[l] + 0.5*mes[l] > pos[j] - 0.5*mes[j] and pos[l] - 0.5*mes[l] <= pos[j] + 0.5*mes[j]):
                    print("overlapping in ", l, j)
                    temp = True
                    break
        # else:
        #     if pos[i]-0.5*mes[i] >= pos[i+2]+0.5*mes[i+2] or pos[i]+0.5*mes[i] <= pos[i+2]-0.5*mes[i+2]:
        #         return True
    return temp