

def h(item, md):
    return divmod(hash(item), md)[1]


class HashTable:
    def __init__(self):
        self.mod = 199
        self.lst = [None] * self.mod
        self.elems = 0

    def __getitem__(self, item):
        return self.lst[h(item, self.mod)][0]

    def __setitem__(self, key, value):
        self.elems += 1

        if not self.lst[h(key, self.mod)]:
            self.lst[h(key, self.mod)] = []

        self.lst[h(key, self.mod)].append(value)


if __name__ == "__main__":
    print('*'*60)
    # print(hash('qwe'))

    htable = HashTable()
    htable['qwe'] = 42
    print(htable['qwe'])

