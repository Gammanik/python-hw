
class ContextManager:
    def __init__(self, outer_self):
        self.outer_self = outer_self

    def __enter__(self):
        self.new_dict = self.outer_self.my_dict.copy()
        return self.new_dict

    def __exit__(self, exc_type, exc_val, exc_tb):
        if not exc_type:
            self.outer_self.my_dict = self.new_dict



class Storage:
    def edit(self):
        return self.cm

    def __init__(self):
        self.cm = ContextManager(self)
        self.my_dict = {'a': 0, 'b': 0, 'c': 0}


if __name__ == '__main__':
    print("----------start")
    s = Storage()

    with s.edit() as se:
        se['a'] = 1
        se['b'] = 2
        print(se)
        print(s.my_dict)
        # raise Exception('should not write')

    print(s.my_dict)






