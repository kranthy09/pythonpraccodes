def square(x):
    return x * x


test_list = [4, 6, 7, 8, 9]

result = map(square, test_list)

print(list(result))

result = map(lambda x: x*x, test_list)


sum = lambda x, y: x+y

print(sum)

print(sum(10, 30))

non = lambda : print("hello")

non()

