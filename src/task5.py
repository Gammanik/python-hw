
def compose_two(f, g):
    return lambda x: f(g(x))


def compose(f, g, *args):
    comp = compose_two(f, g)
    for arg in args:
        comp = compose_two(comp, arg)

    return comp
