
def context_decorator(cls):
    def new_call(self, foo, *args, **kwargs):
        def helper():
            with self:
                return foo()

        return helper

    cls.__call__ = new_call
    return cls


@context_decorator
class PrinterContext:

    def __init__(self, *args):
        print("init printer", self, args)

    def __enter__(self):
        print("Enter")

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Exit")
        return True


@PrinterContext()
def foo():
    print("Inside of function")
    return 42


if __name__ == '__main__':
    print('------------------hey')

    # with PrinterContext():
    #     foo()

    print(foo())
