def get_discr(a, b, c):
    d = b ** 2 - 4 * a * c
    return d

def get_eq_root(a, b, d, order = 1):
    if order == 1:
        x = (-b + d ** (1/2.0)) / (2*a)
    else:
        x = (-b - d ** (1/2.0)) / (2*a)
    return x

def input_param(param = 'a'):
    while True:
        a = raw_input("Enter the parameter of the equation: %s ="
                      % param)
        if a.replace('.', '').isdigit() and float(a) != 0:
            return float(a)
        else:
            print "Please enter the number of nonzero"
