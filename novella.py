import time


def slow_print(text):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(0.03)
    print()


def start_game():
    slow_print("Вы просыпаетесь в темном лесу.")
    slow_print("Как вы здесь оказались? Ваша первая мысль: надо найти выход.")
    choice1()


def choice1():
    slow_print("Вы видите два пути: налево и направо.")
    slow_print("1. Пойти налево")
    slow_print("2. Пойти направо")
    choice = input("Ваш выбор (1 или 2): ")

    if choice == '1':
        left_path()
    elif choice == '2':
        right_path()
    else:
        slow_print("Неверный выбор, попробуйте снова.")
        choice1()


def left_path():
    slow_print("Вы идете налево и находите старую хижину.")
    slow_print("Вы можете войти внутрь или продолжать идти.")
    slow_print("1. Войти в хижину")
    slow_print("2. Продолжить путь")
    choice = input("Ваш выбор (1 или 2): ")

    if choice == '1':
        cabin()
    elif choice == '2':
        slow_print("Вы продолжаете путь и находите лесную поляну.")
        forest_clear()
    else:
        slow_print("Неверный выбор, попробуйте снова.")
        left_path()


def right_path():
    slow_print("Вы идете направо и находите речку.")
    slow_print("Вы можете попытаться пройти через реку или искать мост.")
    slow_print("1. Пройти через реку")
    slow_print("2. Искать мост")
    choice = input("Ваш выбор (1 или 2): ")

    if choice == '1':
        slow_print("Вы преодолели реку, но у вас нет сил продолжать. Игра окончена.")
    elif choice == '2':
        slow_print("Вы находите мост и переходите на другую сторону.")
        slow_print("Впереди вы видите потрясающий замок!")
        castle()
    else:
        slow_print("Неверный выбор, попробуйте снова.")
        right_path()


def forest_clear():
    slow_print("На поляне вы находите разные цветы и замечаете, что один из них светится.")
    slow_print("Вы можете попробовать сорвать цветок или просто отдохнуть.")
    slow_print("1. Сорвать цветок")
    slow_print("2. Отдохнуть")
    choice = input("Ваш выбор (1 или 2): ")

    if choice == '1':
        slow_print("Вы сорвали цветок, но он оказался ядовитым! Игра окончена.")
    elif choice == '2':
        slow_print("Вы отдыхаете и восстанавливаете силы. Внезапно к вам подходит лесной дух!")
        spirit_encounter()
    else:
        slow_print("Неверный выбор, попробуйте снова.")
        forest_clear()


def spirit_encounter():
    slow_print("Лесной дух предлагает вам испытание.")
    slow_print("1. Принять вызов")
    slow_print("2. Отказаться")
    choice = input("Ваш выбор (1 или 2): ")

    if choice == '1':
        slow_print("Вы успешно прошли испытание и получили способность лесного духа!")
        slow_print("Вы продолжаете свое путешествие с новыми силами.")
        right_path()
    elif choice == '2':
        slow_print("Вы отказались от вызова и исчезли в лесу. Игра окончена.")
    else:
        slow_print("Неверный выбор, попробуйте снова.")
        spirit_encounter()


def cabin():
    slow_print("Внутри хижины вы видите старую карту.")
    slow_print("Выберите, что делать дальше.")
    slow_print("1. Взять карту")
    slow_print("2. Уйти из хижины")
    choice = input("Ваш выбор (1 или 2): ")

    if choice == '1':
        slow_print("Вы берете карту и находите путь к сокровищу! Вы победили!")
    elif choice == '2':
        slow_print("Вы выходите на улицу, но в лесу вас ждут опасности. Игра окончена.")
    else:
        slow_print("Неверный выбор, попробуйте снова.")
        cabin()


def castle():
    slow_print("Вы подходите к замку и видите, что двери открыты.")
    slow_print("Внутри вы видите тронный зал.")
    slow_print("1. Войти в тронный зал")
    slow_print("2. Осмотреть окрестности")
    choice = input("Ваш выбор (1 или 2): ")

    if choice == '1':
        slow_print("Вы входите и находите корону! Вы стали королем!")
    elif choice == '2':
        slow_print("Вы сталкиваетесь с охранником и не успеваете убежать. Игра окончена.")
    else:
        slow_print("Неверный выбор, попробуйте снова.")
        castle()


if __name__ == "__main__":
    start_game()