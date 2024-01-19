from random import choice
from os import system

words = {1 : ["манты", "окрошка", "огурец", "ананас", "хошан"], 2 : ["футболка", "шорты", "кепка", "кросовки", "панама"], 3 : ["артем", "игорь", "алекс", "кирилл", "олег"], 4 : ["осел", "рыба", "зебра", "конь", "олень"]}
word = ""

print("Добро пожаловать в мою игру, дружище!\nВыбери категорию\n1.Еда\n2.Одежда\n3.Имя\n4.Животные\n5.Любое слово")
otvet = input()
if otvet == "1":
    word = choice(words[1])
elif otvet == "2":
    word = choice(words[2])
elif otvet == "3":
    word = choice(words[3])    
elif otvet == "4":
    word = choice(words[4])
elif otvet == "5":
    while not word.isalpha():
        print("Кто-то должен ввести слово.")
        word = input().lower()
        system("cls")
    for i in range(100):
        print("")
zagad = ["_"] * len(word)
used = []
lives = 7

while "_" in zagad:
    system("cls")
    print(f"\033[94mCлово: {zagad}\033[0m")
    print(f"\033[91mИспользованные буквы: {used}\033[0m")
    print(f"\033[4mЖизни: {lives}\033[0m")

    print("\033[93mВведите букву\033[0m")
    letter = input().lower()
    if len(letter) == 1 and letter.isalpha():
        if letter in used:
            continue
        if letter in word:
            for i in range(len(word)):
                if letter == word[i]:
                    zagad[i] = letter
            print("\033[92mТакая буква действительно есть!\033[0m")
            used.append(letter)
        else:
            lives -= 1
            print("\033[92mТы ошибся и потерял жизнь.\033[0m")
            used.append(letter)
    else:
        print("Введите одну буковку.")

    if lives == 0:
        print(f"\033[91mНеудачник. Проиграл. Словом было - {word}\033[0m")
        break

if lives != 0:
    print("\033[92mПоздравляю! Ты выиграл игру.\033[0m") 
