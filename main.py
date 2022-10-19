# Stack
my_stack = []


def push(symbol, my_stack):
    my_stack.append(symbol)


def is_correct_brackets(my_stack):
    isEnter = True
    while isEnter:
        count_opening = 0
        count_closing = 0
        text = input('Пожалуйста,введите текст:')
        if text == ' ':
            isEnter = False
            break
        for i in text:
            if i == '(':
                count_opening += 1
                push(i, my_stack)
            if i == ')' and len(my_stack) != 0:
                count_closing += 1
                my_stack.pop()
        if count_opening > count_closing or count_closing > count_opening:
            print('Стек переполнен!!!Проверьте правильность введенных данных\n' +
                  '(Кол-во открывающих скобок должно совпадать с кол-вом закрывающих скобок')

        print(my_stack)
        if isEnter == True:
            my_stack = []


is_correct_brackets(my_stack)


# Recursion

def power(n):
    if (n == 1):
        return (2)
    else:
        return (2 * (power(n - 1)))


def factorial(n):
    if n == 1:
        return n
    else:
        return (n * factorial(n - 1))


fun_arr = []


def fun(n):
    if n == 1:
        fun_arr.append(n)
        return n
    else:
        for i in range(2, n + 1):
            fun_arr.append((i * factorial(i - 1)) / (2 * (power(i - 1) / 2)))
    return ((n * factorial(n - 1)) / (2 * (power(n - 1) / 2)))


print(fun(5))
print(fun_arr)
