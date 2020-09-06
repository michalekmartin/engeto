"""
author = Martin Michálek
"""
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

user_info = dict()
user_info["bob"] = "123"
user_info["ann"] = "pass123"
user_info["mike"] = "password123"
user_info["liz"] = "pass123"

print(40 * "-")
print("Welcome to the app. Please log in:")

username = input("USERNAME: ")
password = input("PASSWORD: ")

if user_info.get(username) != password:
    print("Wrong username or password")
    quit()

print(40 * "-")
print("We have 3 texts to be analyzed.")
text_index = int(input("Enter a number btw. 1 and 3 to select: "))
print(40 * "-")

list_of_words = TEXTS[text_index - 1].split()
total = len(list_of_words)
capital = 0
upper = 0
lower = 0
numeric = 0
summed = 0

for string in list_of_words:
    if string.istitle():
        capital += 1
    if string.isupper():
        upper += 1
    if string.islower():
        lower += 1
    if string.isnumeric():
        numeric += 1
        summed += int(string)

print(f"There are {total} words in the selected text.")
print(f"There are {capital} titlecase words")
print(f"There are {upper} uppercase words")
print(f"There are {lower} lowercase words")
print(f"There are {numeric} numeric strings")
print(40 * "-")

stripped_text = []
for index, word in enumerate(list_of_words):
    word = word.strip(",.")
    stripped_text.append(word)

d = dict()
for word in stripped_text:
    if not len(word) in d:
        d[len(word)] = 0
    d.update({len(word): int(d[len(word)]) + 1})


for number in sorted(d):
    print(number, int(d[number]) * "*", d[number])

print(40 * "-")
print("If we summed all the numbers in this text we would get:", float(summed))
print(40 * "-")
