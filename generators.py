

def loop2():
    for i in range(1, 100000000000):
        yield i*2


l = loop2()

print(next(l))
print(next(l))
print(next(l))
print(next(l))
print(next(l))


generators = (i *2 for i in range(0, 10000000000000))

print(generators)

print(next(generators))
print(next(generators))
print(next(generators))
print(next(generators))
print(next(generators))




def simple():
    for i in range(0, 10000):
        yield i
        print(" i am yeilding")

gen = simple()

for res in gen:
    print(res)




