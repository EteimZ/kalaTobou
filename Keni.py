from math import *

#This simple program can convert english numbers to Ijaw.
print("kalaTobou(version: Keni)")

one = 'Keni'
two = 'Mamu'
three = 'Taru'
four = 'Nein'
five = 'Soron'
six = 'Sondie'
seven = 'Sonoma'
eight = 'Ningina'
nine = 'Ise'
ten = 'Oyi'
f = 'Fini'
twenty = 'Si'
thirty = 'Si-Oyi'
fourty = 'Ma-Si'
fifty  = 'Ma-Si-Oyi'
sixty  = 'Tra-Si'
seventy = 'Tra-Si-Oyi'
eighty = 'Nein-Si'
Ninety = 'Nein-Si-Oyi'
Hundred = 'Sono-Si'


x = eval(input('Please enter a number: '))
 
u = x % 10 
t = x - u

it = ''
ut = ''

if t == 10:
    it = ten
elif t == 20:
    it = twenty
elif t == 30:
    it = thirty
elif t == 40:
    it = fourty
elif t == 50:
    it = fifty
elif t == 60:
    it = sixty
elif t == 70:
    it = seventy
elif t == 80:
    it = eighty
elif t == 90:
    it = Ninety
elif t == 100:
    it = Hundred

if u == 1:
    ut = one
elif u == 2:
    ut = two
elif u == 3:
    ut = three
elif u == 4:
    ut = four
elif u == 5:
    ut = five
elif u == 6:
    ut = six
elif u == 7:
    ut = seven
elif u == 8:
    ut = eight
elif u == 9:
    ut = nine


if x%10 == 0:
    print(it)
elif x > 10:  
    print(it +'-'+ ut + ' fini')
elif x < 10:
    print(ut)
