import math

from sympy.core import singleton


# @singleton
def empty():
    """O(1)"""
    yield from ()


def heapify(value, heap1, heap2):
    l_val, l_size, l_depth = next(heap1, (value, 0, 0))
    r_val, r_size, r_depth = next(heap2, (value, 0, 0))

    curr_min = min(value, l_val, r_val)
    size = l_size + r_size
    depth = max(l_depth, r_depth)

    depth += 1
    size += 1

    if curr_min == value:
        yield (value, size, depth)
        yield empty() if l_size == 0 else heapify(l_val, next(heap1), next(heap1))
        yield empty() if r_size == 0 else heapify(r_val, next(heap2), next(heap2))

    else:
        if r_val < l_val and l_size > 0 and r_size > 0:
            yield (curr_min, size, depth) # curr_min = l_val
            yield empty() if l_size == 0 else heapify(l_val, next(heap1), next(heap1))
            yield empty() if r_size == 0 else \
                heapify(value, next(heap2), next(heap2))
        else:
            yield (l_val, size, depth)
            yield empty() if l_size == 0 else \
                heapify(value, next(heap1), next(heap1))
            yield empty() if r_size == 0 else \
                heapify(r_val, next(heap2), next(heap2))


# 3
def print_heap(heap, prefix=''):
    val, size, depth = next(heap, (-1, 0, 0))

    if val == -1:
        pass
    else:
        print("{s}[{sz}, {dp}]: {v}".format(s=prefix, v=val, dp=depth, sz=size))
        print_heap(next(heap), prefix + "    ")
        print_heap(next(heap), prefix + "    ")


# 4
def build_heap(seq):
    seq = list(seq)
    n = len(seq)

    if n > 0:
        for i in range(n-1, -1, -1):
            if n > 2 * i + 2:
                seq[i] = heapify(seq[i], seq[2 * i + 1], seq[2 * i + 2])
            elif n > 2 * i + 1:
                seq[i] = heapify(seq[i], seq[2 * i + 1], empty())
            else:
                seq[i] = heapify(seq[i], empty(), empty())

        yield next(seq[0])
        yield next(seq[0])
        yield next(seq[0])

    else:
        empty()


# 5
def extract_last(heap):
    pass


# 6
def extract_min(heap):
    pass


# 7
def heap_sort(seq):
    pass


# 8
def bench():
    pass


