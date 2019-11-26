
class UML(type):
    dc = {}

    def draw_uml(cls):

        if not isinstance(cls, UML):
            raise TypeError('class: ', cls.__name__, "is not an UML type")

        def draw_level(lvl, cls_name):
            """
                or I could've just use cls.__subclasses__()
                and avoid creating UML.dc
            """
            print(lvl * 4 * ' ' + cls_name)

            for kid_name in UML.dc[cls_name]:
                draw_level(lvl + 1, kid_name)

        draw_level(0, cls.__name__)

    def __new__(mcs, name, bases, attrs, **kwargs):
        UML.dc[name] = []

        for base in bases:
            UML.dc[base.__name__].append(name)

        return super().__new__(mcs, name, bases, attrs)
