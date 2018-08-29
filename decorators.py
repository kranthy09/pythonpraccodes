def closure(a):
    def inner():
        print("calling printing function")
        return a()
    return inner



def printing():
    print('hello')

inner = closure(printing)

inner()

def closure2(func):
    def inner(a,b):
        print("i am calling"+ func.__str__())
        return func(a, b)
    return inner

def sub(a, b):
    return a-b

inner = closure2(sub)

result = inner(20, 10)

print(result)



@closure2
def sub(a, b):
    return a-b


result = sub(20, 10)
print(result)



# <h><i>Pavan</i></h>


def itag(func):
    def inner():
        phone = func()
        country_code = api.request(phone)
        return country_code, phone

        return "<i>" + func() + "</i>"
    return inner

def htag(func):
    def inner():
       return "<h>" + func() + "</h>"
    return inner

@htag()
@itag
def printing_pavan():
    return "pavan"

res = printing_pavan()
print(res)