# Домашнее задание №2

**Дедлайны**: 17.09.2019 12:10

Перед сдачей задания необходимо ознакомиться с информацией по 
[ссылке](https://gitlab.com/itmo-scripting-languages/python-2019/blob/master/README.md).

## Задачи

#### 1. Функции фибоначчи (1.5 балла)
Написать функцию `fib3` таким образом, чтобы после ее вызова можно было вызвать `fib4`. В свою очередь, после 
вызова `fib4` должен быть возможен вызов функции `fib5`.

Сами функции должны возвращать соответствующие числа Фибоначчи.
```
>>> fib1()
1
>>> fib2()
1
>>> fib3()
2
>>> fib4()
3
>>> fib5()
5
```


Объявлять функции `fibN` с номером N > 4 запрещено. 

#### 2. Что-то пошло не так (1 балл) 
Алексей написал следующий код:
```python
def factory(n):
    list_to_return = []
    for i in range(n):
        list_to_return.append(lambda: i)
    return list_to_return 
```
но его код работает не так, как он ожидал:
```python
>>> for func in factory(5):
        print(func())
4
4
4
4
4
```
Вам предстоит:
- объяснить Алексею (заодно и Дмитрию!) почему так получилось в 2-4 предложениях (0.5 балла)
- переписать код метода factory так, чтобы исправить проблему (0.5 балла)

#### 3. Union (0.5 балла)
Реализуйте функцию union, возвращающую объединение произвольного числа множеств.
```python
>>> union({1, 2, 3}, {10}, {2, 6})     
{1, 2, 3, 6, 10}
```
 
#### 4. НОК (0.5 балла)
Напишите функцию lcm, вычисляющую НОК (наименьшее общее кратное) двух и более
 целых чисел.
```python
>>> lcm(100500, 42) 
703500
>>> lcm(*range(2, 40, 8)) 
19890
```  
 
#### 5. Compose (0.5 балла)
Реализуйте функцию compose, которая принимает две и более функции от одного аргумента, и возвращает их композицию.
```python
>>> f = compose(lambda x: 2 * x, lambda x: x + 1, lambda x: x % 9) 
>>> f(42)
14
>>> 2 * ((42 % 9) + 1)
14
```



#### 6. Хаскеллолисп (4 балла)
Написать связные списки и функции для работы с ними в хаскелло-лисповском стиле.
Список самих функций можно найти в соответствующей заготовке. Тесты, как обычно, лежат 
в соответствующем файле в директории tests.

Примечания:
  * Для реализации `Nil` и `Cons` необходимо использовать контейнер `namedtuple` из библиотеки `collections`.
  * Нельзя использовать циклы. Нельзя менять один раз созданную переменную.


#### 7. List comprehension is <..>er? (1 балл)
Язык python поддерживает списочные встраивания ([list comprehensions](https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions)),  
вспомним их синтаксис на примере создания списка квадратов четных чисел из промежутка от 1 до 9:
```python
squares = [x**2 for x in range(1, 10) if x % 2 == 0]
```

В этой задаче вам предстоит с помощью  [timeit](https://docs.python.org/3.7/library/timeit.html), показать быстрее или медленнее
применение map/filter по сравнению с эквивалентным list comprehension. 

#### 8. Prime time (1 балл)
Напишите списковое выражение, генерирующее все простые числа не больше заданного числа.