
def factory(n):
    list_to_return = []

    ''' 
    the problem was that loop does not create a new scope in python
    I've used an approach from:
    https: //docs.python.org/3/faq/programming.html#why-do-lambdas
    -defined-in-a-loop-with-different-values-all-return-the-same-result
    
    to fix it
    '''
    for i in range(n):
        list_to_return.append(lambda j=i: j)
    return list_to_return


if __name__ == '__main__':
    for func in factory(5):
        print(func())
