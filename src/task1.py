
def to_snake(name):
    new_name = list()
    new_name.append(name[0])

    for i in range(1, len(name)):
        if (name[i - 1].islower() or name[i - 1].isdigit()) and name[i].isupper():
            new_name.append('_')
            new_name.append(name[i].lower())
        else:
            new_name.append(name[i].lower())

    return ''.join(new_name)


class Pepifize(type):
    def __new__(mcs, name, bases, attrs, **kwargs):
        new_attrs = {}

        for atr in attrs:
            if callable(attrs[atr]) and atr not in kwargs['ignore']:
                new_attrs[to_snake(atr)] = attrs[atr]
            else:
                new_attrs[atr] = attrs[atr]

        return super().__new__(mcs, name, bases, new_attrs)
