

x = 50
def func():
    print 'x is', x
    x = 2
    print 'Changed local x to', x
func()
print 'x is still', x
print '*'*20
def func2():
    global x

    print 'x is', x
    x = 2
    print 'Changed local x to', x

x = 50
func2()
print 'Value of x is', x