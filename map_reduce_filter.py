import functools

test_list = [1, 2, 3, 4 , 5 , 6]




def square(x):
    return x*x



def even(x):
    return x %2 == 0


def sum(x, y):
    return x+y


result = map(square, test_list)

print(result)

print(list(result))


result = filter(even, test_list)

print(list(result))

result = functools.reduce(sum, test_list)

print(result)
