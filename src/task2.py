

def h(item, md):
    return hash(item) % md


class HashTable:
    def __init__(self):
        self.sz = 101
        self.lst = [None] * self.sz
        self.deleted = [True] * self.sz
        self.elems = 0

    def __getitem__(self, item):
        if self.deleted[h(item, self.sz)]:
            raise KeyError(item)

        return self.lst[h(item, self.sz)][-1][1]

    def __setitem__(self, key, value):
        self.elems += 1

        if not self.lst[h(key, self.sz)]:
            self.lst[h(key, self.sz)] = []

        self.deleted[h(key, self.sz)] = False
        self.lst[h(key, self.sz)].append((key, value))

    def __delitem__(self, key):
        self.elems -= 1

        if len(self.lst[h(key, self.sz)]) == 1:
            self.deleted[h(key, self.sz)] = True
            # del self.lst[h(key, self.sz)]
        else:
            del self.lst[h(key, self.sz)][-1]

    def keys(self):
        # return [[self.lst[i][j] for j in range(len(self.lst))] for i in range(self.sz) if not self.deleted[i]]
        # return [self.lst[i] for i in range(self.sz) if not self.deleted[i]]
        return map(lambda x: x[0], self.items())

    def items(self):
        for i in range(0, self.sz):
            if not self.deleted[i]:
                for j in self.lst[i]:
                    yield j

    def __contains__(self, item):
        return not self.deleted[h(item, self.sz)]

    def __len__(self):
        return self.elems


if __name__ == "__main__":
    print('*'*60)
    # print(hash('qwe'))

    htable = HashTable()
    htable['qwe'] = 42
    htable['qwe'] = 55
    htable['ex'] = 40
    print(htable['qwe'])
    print()

    del htable['qwe']
    print(htable['qwe'])

    print('a' in htable)
    print('qwe' in htable)

    for key in htable.keys():
        print(key)

    for key, value in htable.items():
        print(key, value)

    print(len(htable))
