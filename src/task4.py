from timeit import default_timer as timer


class Timer:

    def __enter__(self):
        self.start = timer()

    def __exit__(self, exc_type, exc_val, exc_tb):
        print(exc_type, "val: ", exc_val, "td: ", exc_tb)

        if not exc_type is None:
            print("finished with exception ", exc_val, " elapsed: ", (timer() - self.start))
        else:
            print("elapsed: ", (timer() - self.start))

        return True


if __name__ == "__main__":
    cnt = 1

    with Timer() as tm:
        for i in range(0, 100000):
            cnt += 1