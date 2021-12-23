# Swapping two variable program

def swap1(a, b):
    print("Before Swaaping: a = " + str(a) + " b = " + str(b))
    a, b = b, a
    print("After Swaaping: a = " + str(a) + " b = " + str(b))


def swap2(a, b):
    print("Before Swaaping: a = " + str(a) + " b = " + str(b))
    temp = a
    a = b
    b = temp
    print("After Swaaping: a = " + str(a) + " b = " + str(b))


def swap3(a, b):
    """ Swap by using extra variable"""
    print("Before Swaaping: a = " + str(a) + " b = " + str(b))
    c = a + b
    a = c - a
    b = c - b
    print("After Swaaping: a = " + str(a) + " b = " + str(b))


swap1(4, 5)
swap2(4, 5)
swap3(4, 5)
