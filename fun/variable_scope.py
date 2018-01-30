g = "Global"


def fun():
    l = "Local"
    print(l, g)


def fun2():
    global g
    g = "Changed in fun2"  # local variable
    print(g)


fun2()
fun()
