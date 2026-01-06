point = (0, 7)

match point:
    case (0, 0):
        print("Origin")
    case (0, y):
        print("Y =", y)
    case (x, 0):
        print("X =", x)
    case (x, y):
        print("X, Y =", x, y)
    case _:
        print("Not a point")
