
class ContextManager:
    def __init__(self, s_dict):
        self.cm_dict = s_dict
        self.to_delete = {}

    def __enter__(self):
        self.buffer = {}
        return self

    def __getitem__(self, item):
        return self.buffer[item]

    def __setitem__(self, key, value):
        self.buffer[key] = value

        # in case we've deleted an element and then assigned it again
        if key in self.to_delete:
            del self.to_delete[key]

    def __delitem__(self, key):
        if key in self.cm_dict:
            self.to_delete[key] = key
        else:
            raise KeyError("item is not in dict")

    def __exit__(self, exc_type, exc_val, exc_tb):
        if not exc_type:
            for key in self.buffer:
                self.cm_dict[key] = self.buffer[key]

            for key in self.to_delete.keys():
                del self.cm_dict[key]

            self.to_delete.clear()


class Storage:
    def edit(self):
        return ContextManager(self.my_dict)

    def __init__(self):
        self.my_dict = {}

    def __getitem__(self, item):
        return self.my_dict[item]

    def __setitem__(self, key, value):
        raise TypeError("item could be set only in Context manager")

    def __str__(self):
        return str(self.my_dict)

    def __delitem__(self, key):
        raise TypeError("item could be deleted only in Context manager")







