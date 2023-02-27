import time

a = True
b = True


def test():
    global a
    global b
    while a:
        print("1")
        time.sleep(3)
        print("2")
        time.sleep(5)
        a = False
    while b:
        print("a")
        time.sleep(3)
        print("b")
        b = False


test()
