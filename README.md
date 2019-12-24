### Лекционная контрольная работа №3

Вам предстоит создать метакласс `Dictator`, который позволит контролировать рождаемость объектов.

#### id 
Первое, что необходимо сделать - добиться того, чтобы все создаваемые объекты классов с метаклассом `Dictator` 
автоматически получали бы поле `id`. `id` является номером объекта, каждый следующий объект должен получать `id` на 
единицу больше, чем прошлый созданный объект **этого** класса.

```python
class A(metaclass=Dictator):
    pass
class B(metaclass=Dictator):
    pass

a1 = A()
b1 = B()
a2 = A()

print(a1.id)
print(b1.id)
print(a2.id)

# Будет выведено
1
1
2
```

#### log 
Следующеее, что хочется научиться делать - отслеживать где и когда были созданы объекты. Т.е. необходимо написать статический
метод `Dictator.show_log`, который будет **генератором** и будет выдавать информацию о цепочке рождения (примеры ниже).

Если его вызвать без параметров, то должна быть получена информация обо всех объектах классов с данным метаклассом.
Если вызвать с параметром - классом, то должна быть получена информация обо всех объектах этого класса. 
Если же переданный класс имеет другой метакласс, то должно быть сгенерировано исключение.

**Примечание**: в цепочке рождения должны присутствовать только функции из классов с метаклассом `Dictator`. 
Остальные могут быть опущены.


Метод `Dictator.clear_log` должен очищать информацию о рождении. Если вызван без параметров, то всех классов. 
Если с параметром - классом, то необходимо очистить информацию о его объектах.

```python
class A(metaclass=Dictator):
    pass

a = A()
aa = A()

for log in Dictator.show_log(A):
    print(log)
    
    
# будет выведено
A.id1: ...
A.id2: ...

Dictator.clear_log()

class A(metaclass=Dictator):
    def __init__(self, x):
        print(x)

class B(metaclass=Dictator):
    def foo(self, y):
        tmp = A(y)
    def bar(self):
        self.foo(3)
        
b = B()
print(b.id)
b.bar()

for log in Dictator.show_log():
    print(log)
    
    
# Будет выведено
1 # вывод print(b.id)
3 # вывод print(x)
B.id1: ...
A.id1: ... | B.id1.bar -> B.id1.foo


Dictator.clear_log()

class A(metaclass=Dictator):
    def __init__(self, b):
        b.bar()

class B(metaclass=Dictator):
    def foo(self, y):
        tmp = C()
    def bar(self):
        self.foo(3)

class C(metaclass=Dictator):
    pass
        
c = C()
b1 = B()
b2 = B()
a = A(b2) 
    
for log in Dictator.show_log():
    print(log)
    
    
# Будет выведено
C.id1: ...
B.id1: ...
B.id2: ...
A.id1: ...
C.id2: ... | A.id1._ _init_ _ -> B.id2.bar -> B.id2.foo
```
#### Дополнительное задание (4 балла)
Необходимо сделать так, чтобы у каждого класса с метаклассом  `Dictator` был статический метод `free_context`. 
Этот метод должен возвращать менеджер контекста. Данный менеджер контекста позволяет не учитывать созданные внутри with-блока
объекты в логе рождаемости.  

```python
class A(metaclass=Dictator):
    def __init__(self, x):
        pass

class B(metaclass=Dictator):
    def foo(self, y):
        tmp = A(y)
    def bar(self):
        self.foo(3)
        
b = B()
b.bar()

with B.free_context():
    B()
    b.bar()

for log in Dictator.show_log():
    print(log)

# Будет выведено
B.id1: ...
A.id1: ... | B.id1.bar -> B.id1.foo
```
