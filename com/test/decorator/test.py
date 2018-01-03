def decorator_a(func):
    print 'Get in decorator_a'
    def inner_a(*args, **kwargs):
        print 'Get in inner_a'
        return func(*args, **kwargs)
    return inner_a

def decorator_b(func):
    print 'Get in decorator_b'
    def inner_b(*args, **kwargs):
        print 'Get in inner_b'
        return func(*args, **kwargs)
    return inner_b

@decorator_b
@decorator_a
def f(x):
    print 'Get in f'
    return x * 2

def f1(x):
    print 'Get in f1'
    return x * 2

print f(1)

print decorator_b(decorator_a(f1(1)))