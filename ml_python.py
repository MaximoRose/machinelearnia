
import math
from pickletools import read_uint1
from unittest import result


Phi = (1+math.sqrt(5))/2
PhiPrime = -1/Phi

# VIDEO 2
# https://www.youtube.com/watch?v=doFpNjdmsw8&list=PLO_fdPEVlfKqMDNmCFzQISI2H_nJcEDJq&index=2
# f(x,y) = x^2 + y s'ecrit :
f = lambda x,y : x**2 + y

def e_potentielle(masse,hauteur, e_limite, g = 9.81) :
    E = masse * hauteur * g
    e_depasse = False
    if (E > e_limite) :
        e_depasse = True
    # Lui il voulait qu'on retourne le bool de la forme "return E < e_limite"
    return E, e_depasse

# VIDEO 3
# https://youtu.be/x_Jeyvw7n9I
def loop_decroiss(start, stop, pas) :
    for i in range (start, stop, pas) :
        print(i)
    return

# exo video 3
def fibonnaci(n) :
    fib = 0
    resultat = []
    cnt = 0
    while (fib < n) :
        fib = (1/math.sqrt(5))*(Phi**cnt - PhiPrime**cnt)
        resultat.append(fib)
        cnt += 1
    # retourne la suite de fibonacci jusqu'a n
    return resultat
# son fibo :
def correction(n) :
    a = 0
    b = 1
    # HYPER PRATIQUE POUR REPRESENTER DES SUITES. Surement plus performant que moi
    # Surtout que moi je travaille avec des float comme j'ai des sqrt()
    while a < n :
        print(a)
        a ,b = b, a+b
# exo video 4
def exo_video_4(n) :
    a = 0
    b = 1
    resultat = [a]
    while a < n :
        a, b = b, a + b
        resultat.append(a)
    return resultat

# VIDEO 4
# https://www.youtube.com/watch?v=5UOSiCPu5aM
# Par rapport a une liste, le tuple est protege : on ne peut pas le modifier
# Il est aussi plus rapide a remplir qu'une liste quand on gere beaucoup de valeurs
tuple_1 = (1, 2, 4, 5)
# string, liste et tupple, permettent de creer des sequences d'informations, des infos ordonnees
# Pour acceder a un ensemble fini d'element de notre sequence : Liste[debut:fin:pas]

print(f(5,3))

masse = 65
hauteur = 2300
g = 9.81

energie, isabove = e_potentielle(masse=masse, hauteur=hauteur, e_limite = 1000)
loop_decroiss(start = 10, stop = -10, pas = -2)

fibo = fibonnaci(10)
print(fibo)
# SLICING : on ne prend que les 2 premiers elements : index 0 et 1
print(fibo[:2])
print()
# SLICING : on ne prend qu'a partir du troisieme
print(fibo[2:])
# SLICING : On ne prend que un sur deux
print(fibo[::2])
# SLICING : Extraire tous mes elements a l'envers
print(fibo[::-1])
print()
print(energie, 'Joules')
print(isabove)



