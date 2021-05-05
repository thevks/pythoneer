def ref_demo(x) :
    print("x=", x," id=", id(x))
    x = 42
    print("x=", x," id=", id(x))

def foo(l) :
    l += [47, 11]
    

if __name__ == '__main__' :
    x = 10
    print("x=", x," id=", id(x))
    ref_demo(x)

    list = [1, 2, 3, 4, 5, 6]
    print(list)
    foo(list)
    print(list)

    foo(list[:])
    print(list)