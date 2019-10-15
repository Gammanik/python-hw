i = 4


def fib1():
    return 1


def fib2():
    return 1


def fib3():
    globals()['fib' + '4'] = \
        lambda: globals()['fib' + '3']() + globals()['fib' + '2']()
    return fib1() + fib2()


def helper():


    globals()['fib' + str(globals()['i'])] = \
        lambda: globals()['fib' + str(globals()['i'] - 1)]() \
        + globals()['fib' + str(globals()['i'] - 2)]()

    globals()['i'] = globals()['i'] + 1


    return \
        lambda: globals()['fib' + str(globals()['i'] - 1)]() \
        + globals()['fib' + str(globals()['i'] - 2)]()



# globals()['fib' + '5'] = helper()



    # lambda: globals()['fib' + '4']() + globals()['fib' + '3']()

# def fib4():
#     return fib3() + fib2()




if __name__ == '__main__':
    print(fib3())
    print(fib4())
    # print(fib6())
    # print(fib5())
    # print(fib6())

    helper()
    helper()
    helper()
    helper()
    helper()

    # print('shit: ', fib6())

    print('here we go: ', helper()())

# fibonacci = lambda x : 0 if x==0 else 1 if 0 < x <= 2 else fibonacci(x-1) + fibonacci(x-2)
