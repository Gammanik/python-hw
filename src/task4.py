
def lcm_two(a, b):
    orig1 = a
    orig2 = b

    while a != b:
        if a > b:
            a = a-b
        else:
            b = b-a

    return orig1 / a * orig2


def lcm(a, b, *xs):
    nok = lcm_two(a, b)

    for x in xs:
        nok = lcm_two(nok, x)

    return nok
