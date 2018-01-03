def spamrun(fn):
    def sayspam(*args):
        print "spam,spam,spam"
    return sayspam
    
@spamrun
def useful(a,b):
    print a**2+b**2


if __name__ == '__main__':
    # test_get()
    useful(3,4)