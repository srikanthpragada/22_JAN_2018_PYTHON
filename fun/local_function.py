gv = "global"


def fun():
    print("I am in fun()")
    ev = "enclosing"

    def lfun():
        lv = "local"
        nonlocal ev
        ev = "New value for enclosing variable "
        print("I am in local function")
        print(gv, ev, lv)

    print("I am again in fun()")
    lfun()
    print(ev)


fun()
