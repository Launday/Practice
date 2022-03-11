import os


def fib_find(digit):
    sequence = [0, 1]
    i = 1
    while sequence[i] <= digit:
        sequence.append(sequence[i] + sequence[i - 1])
        i += 1
    return sequence


def get_input():
    os.system('cls')
    digit = input("Введите число, больше которого должно быть число в последовательности Фибоначчи: ")
    if len(digit.split()) != 1:
        print("Ввести нужно ровно одно число!")
        os.system("PAUSE")
        digit = get_input()
    elif not digit.isdigit():
        print("Ввести требуется именно число.")
        os.system("PAUSE")
        digit = get_input()
    return int(digit)


def show_output(digit, number, quantity):
    print(
        "Первое число в последовательности Фибоначчи большее {} равняется {}\nЭто {} число в последовательности.".format(
            digit, number, quantity))


def menu():
    print("1 - Найти число Фибоначчи\n2 - Посмотреть историю поиска\n3 - Выход\n")
    option = input("Введите одну из предложенных команд: ")
    os.system('cls')
    if len(option.split()) != 1:
        print("Ввести требуется одно число!")
        option = menu()
    elif not option.isdigit():
        print("Введенное команда должна быть числом!")
        option = menu()
    elif int(option) not in (1, 2, 3):
        print("Введенное число должно быть одной из команд!")
        option = menu()
    return int(option)


def save_history(digit, number, quantity):
    global condition, position, answer, counter
    condition.append(digit)
    answer.append(number)
    position.append(quantity)
    counter += 1


def show_history():
    global condition, position, answer, counter
    for i in range(counter):
        print(
            "Число в последовательности Фибоначчи большее {} равнялось {}. Это было {} число в последовательности.".format(
                condition[i], answer[i], position[i]))
    os.system("PAUSE")


def main():
    os.system('cls')
    option = menu()
    if option == 1:
        digit = get_input()
        sequence = fib_find(digit)
        show_output(digit, sequence[-1], len(sequence))
        save_history(digit, sequence[-1], len(sequence))
        os.system("PAUSE")
        main()
    elif option == 2:
        show_history()
        main()
    elif option == 3:
        print("\nХорошего Дня!\n")
        os.system("PAUSE")
        return


if __name__ == '__main__':
    global condition, position, answer, counter
    condition = []
    position = []
    answer = []
    counter = 0
    main()
