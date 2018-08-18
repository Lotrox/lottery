#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: Daniel Martinez Caballero
# Description: Simulación de Loteria de Navidad. Dados uno o más boletos, 
#		se realizará una simulación anual hasta conseguir ser premiado.
# Args: Debe introducir con espacios los décimos a jugar.

import sys, random, time
from datetime import date

age = date.today().year # Año de inicio de la simulación.

numNumber = len(sys.argv) - 1

if numNumber < 1:
        print "Error, debes introducir al menos un número"
        sys.exit()

loser = True
money = 0
name  = "None"
prize = 0

def check():
        rand = int(round(random.random()*99999))
        for i in range(numNumber):
                #print str(rand ) + " --- " + str(int(sys.argv[i+1]))
                if rand == (int(sys.argv[i+1])):
                        return True
        return False

while loser:
        time.sleep(0.01)
        money += numNumber*20
        if check():
                prize = 400000
                name  = "El gordo"
                loser  = False
        if check():
                prize = 125000
                name  = "Segundo Premio"
                loser  = False
        if check():
                prize = 50000
                name  = "Tercer Premio"
                loser  = False
        for i in range(2):
                if check():
                        prize = 20000
                        name  = "Cuarto Premio"
                        loser  = False
        for i in range(8):
                 if check():
                        prize = 6000
                        name  = "Quinto Premio"
                        loser  = False
        if loser:
                print "Año " + str(age) + " - \"Lo importante es la salud\""
        else:
                print "Año " + str(age) + " - \"¡HA TOCADO!\""
        age += 1

print "Has gastado un total de " + str(money) + "€ y finalmente te ha tocado " + name + " valorado en " + str(prize) + "€"
print "Beneficio: " + str(prize - money) + "€"
