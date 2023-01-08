# -*- coding: utf-8 -*-
"""
Created on Sat Jan  7 20:48:17 2023

@author: oardila
"""

'''
 * Escribe un programa que reciba un texto y transforme lenguaje natural a
 * "lenguaje hacker" (conocido realmente como "leet" o "1337"). 
 * Se utilizó la siguiente tabla (https://www.gamehouse.com/blog/leet-speak-cheat-sheet/)
* Dado que la letra ñ o Ñ no tiene cambio se optó por dejar la misma letra 
 *   con el alfabeto y los números en "leet".

'''

abc = {
    "A":"4",
    "B":"|3",
    "C":"[",
    "D":")",
    "E":"3",
    "F":"|=",
    "G":"&",
    "H":"#",
    "I":"1",
    "J":",_|",
    "K":">|",
    "L":"1",
    "M":"/\\/\\",
    "N":"^/",
    
    "O":"0",
    "P":"|*",
    "Q":"(_,)",
    "R":"I2",
    "S":"5",
    "T":"7",
    "U":"(_)",
    "V":"\\/",
    "W":"\\/\\/",
    "X":"><",
    "Y":"j",
    "Z":"2",
    "1":"L",
    "2":"R",
    "3":"E",
    "4":"A",
    "5":"S",
    "6":"b",
    "7":"T",
    "8":"B",
    "9":"g",
    "0":"o",
    " ":" ",
}

normal_word = input("¿Ingresa el texto que quieras transformar y enter? ").upper()
word_leet = ""

for i in range(len(normal_word)):
    if normal_word[i]=="Ñ":
        speel="Ñ"
        result = speel
        word_leet += result
    else:    
        speel = normal_word[i]
        result = speel.replace(speel, abc[speel])
        word_leet += result
print("La traducción en lenguaje leet es: ", word_leet)