def calc():
    while True:
        b = input("Сложить: +\n"
              "Вычесть: -\n"
              "Умножить: *\n"
              "Поделить: /\n"
              "Выйти: 0\n"
              "Выберите команду: ")
        if b == '0':
            print("Выход из программы")
            break
        a = int(input("Введите число: "))
        c = int(input("Введите число: "))
        if b == '+':
            print("Равно:", a + c)
        elif b == '-':
            print("Равно:", a - c)
        elif b == '*':
            print("Равно:", a * c)
        elif b == '/':
            if c != 0:
                print("Равно:", a / c)
            else:
                print("На ноль делить нельзя!")

calc()