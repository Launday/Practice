def exponentiation(variables):
    return variables[0] ** variables[1]


def get_input():
    variables = input("Введите число и его степень: ").split()
    if len(variables) != 2:
        print("Введите ровно две переменные! ")
        variables = get_input()
    if variables[0].isdigit() == False or variables[1].isdigit() == False:
        print("Введите два числа! ")
        variables = get_input()
    variables = [int(variables[0]), int(variables[1])]
    return variables


def show_output(res, variables):
    print("{} ^ {} = {}".format(variables[0], variables[1], res))


if __name__ == '__main__':
    variables = get_input()
    result = exponentiation(variables)
    show_output(result, variables)
