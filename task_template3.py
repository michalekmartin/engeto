'''
author = Martin
'''
TEXTS = ['''
Situated about 10 miles west of Kemmerer, 
Fossil Butte is a ruggedly impressive 
topographic feature that rises sharply 
some 1000 feet above Twin Creek Valley 
to an elevation of more than 7500 feet 
above sea level. The butte is located just 
north of US 30N and the Union Pacific Railroad, 
which traverse the valley. ''',

'''At the base of Fossil Butte are the bright 
red, purple, yellow and gray beds of the Wasatch 
Formation. Eroded portions of these horizontal 
beds slope gradually upward from the valley floor 
and steepen abruptly. Overlying them and extending 
to the top of the butte are the much steeper 
buff-to-white beds of the Green River Formation, 
which are about 300 feet thick.''',

'''The monument contains 8198 acres and protects 
a portion of the largest deposit of freshwater fish 
fossils in the world. The richest fossil fish deposits 
are found in multiple limestone layers, which lie some 
100 feet below the top of the butte. The fossils 
represent several varieties of perch, as well as 
other freshwater genera and herring similar to those 
in modern oceans. Other fish such as paddlefish, 
garpike and stingray are also present.'''
]

print("-" * 40)
print("Welcome to the app. Please log in:")

users = {"bob": "123", "ann": "pass123", "mike": "password123", "liz": "pass123"}

username = input("USERNAME: ")
password = input("PASSWORD: ")

if not users[username] == password:
    print("Wrong username or password")
    quit()

print("-" * 40)
print(f"We have {len(TEXTS)} texts to be analyzed.")
number = int(input(f"Enter a number btw. 1 and {len(TEXTS)} to select: ")) - 1
print("-" * 40)

list_of_words = TEXTS[number].split()

words = 0
title = 0
upper = 0
lower = 0
numeric = 0
summed = 0
dic = {}

while list_of_words:
    word = list_of_words.pop(0).strip(" .,")
    words += 1
    key = len(word)
    if key not in dic:
        dic.update({key: 1})
    elif key in dic:
        dic[key] += 1
    if word.istitle():
        title += 1
    elif word.isupper():
        upper += 1
    elif word.islower():
        lower += 1
    elif word.isnumeric():
        numeric += 1
        summed += int(word)

print(f"There are {words} words in the selected text.")
print(f"There are {title} titlecase words.")
print(f"There are {upper} uppercase words.")
print(f"There are {lower} lowercase words.")
print(f"There are {numeric} numeric strings.")
print("-" * 40)

keys = sorted(list(dic))
while keys:
    key = keys.pop(0)
    if key < 10:
        print("", key, "*" * dic[key], dic[key])
    else:
        print(key, "*" * dic[key], dic[key])

print("-" * 40)
print("If we summed all the numbers in this text we would get:", summed)
print("-" * 40)
