import timeit


def cmp_filter_map():
    t1 = timeit\
        .timeit("[x**2 for x in range(1, 10000) if x % 2 == 0]", number=1000)

    t2 = timeit\
        .timeit("map(lambda x: x**2, "
                "filter(lambda x: x % 2 == 0, range(1, 10000)))", number=1000)
    return t2 - t1


if __name__ == '__main__':
    time = cmp_filter_map()
    print("list comprehension is faster than map by: {0} seconds".format(time))
