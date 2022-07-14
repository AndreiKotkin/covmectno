from random import randint
import math

def human_guess():
    lower = int(input("Введите нижнюю границу:- "))
    upper = int(input("Введите верхнюю границу:- "))

    x = randint(lower, upper)
    print("\n\tУ тебя всего лишь ",
          round(math.log(upper - lower + 1, 2)),
          " три попытки, чтобы угадать число!\n")

    count = 0

    while count < math.log(upper - lower + 1, 2):
        count += 1
        guess = int(input("Твоя догадка:- "))
        if x == guess:
            print("Поздравляю! Число угадано за ",
                  count, " попытки(ок)")
            break
        elif x > guess:
            print("Загаданное число больше твоего!")
        elif x < guess:
            print("Загаданное число меньше твоего!")

    if count >= math.log(upper - lower + 1, 2):
        print("\nЗагаданное число: %d" % x)
        print("\tПопробуй в следующий раз!")

def computer_guess():
    A = int(input("Введите нижнюю границу: "))
    B = int(input("Введите верхнюю границу: "))
    time = int(input("Количество попыток: "))

    while time != 0:
        ran = randint(A, B)
        inp = input(f"Загаданное число - {ran} ? ")
        time -= 1
        if inp == "y":
            print("Компьютер угадал!")
            break
        if time == 0:
            print("Компьютер не угадал число!")
            break

print("Игра угадай число!")
while True:
    print("Кто будет угадывать?")
    print("1 - Человек")
    print("2 - Компьютер")
    print("0 - Выход")
    command = int(input("Введите номер команды: "))
    if command == 1:
        human_guess()
    elif command == 2:
        computer_guess()
    elif command == 0:
        break


