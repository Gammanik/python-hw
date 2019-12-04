
class FixedSizeQueue(list):
    def __init__(self, maxlen: int):
        super(FixedSizeQueue, self).__init__()
        self.maxlen = maxlen
        self.empty = True
        self.full = False

    def _check_sizeflags(self):
        self.empty = self._is_empty()
        self.full: bool = self._is_full()

    @property
    def _is_empty(self):
        return len(self) == 0

    def _is_full(self):
        return len(self) == self.maxlen

    def put(self, value):
        if self.full:
            raise ValueError
        self.insert(0, value)
        self._check_sizeflags()

    def get(self):
        if self.empty:
            raise ValueError
        self.pop(-1)
        self._check_sizeflags()




if __name__ == "__main__":
    q = FixedSizeQueue(maxlen=10)
    print(q.empty)
    q.put(22)
    print(q.get())
    print(len(q))
