words = ["python", "programmation", "langage", "ordinateur", "apprentissage"]

vowels = ["a", "e", "u", "i", "o", "y"]

list=[]


for word in words:
    nb_vowels = 0
    for lettre in word:
        if lettre in vowels:
            nb_vowels = nb_vowels +1
    list.append((word, nb_vowels))

print(list)