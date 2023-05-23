def quadratic_equation_solver():
    import cmath as cm
    import numpy as np
    
    a = float(input("Input the \"a\" variable: "))
    b = float(input("Input the \"b\" variable: "))
    c = float(input("Input the \"c\" variable: "))

    if a == 0:
        print("Not a quadratic equation!")
        quit()

    if b ** 2 - 4 * a * c < 0:
        x = (-b + cm.sqrt(b ** 2 - 4 * a * c)) / (2 * a)
        y = (-b - cm.sqrt(b ** 2 - 4 * a * c)) / (2 * a)
        print("Solutions are: ", x, ",", y)
        quit()

    if b ** 2 - 4 * a * c >= 0:
        x = (-b + np.sqrt(b ** 2 - 4 * a * c)) / (2 * a)
        y = (-b - np.sqrt(b ** 2 - 4 * a * c)) / (2 * a)
        if x == y:
            print("Solution is", x)
        else:
            print("Solutions are: ", x, ",", y)
        quit()

quadratic_equation_solver()
