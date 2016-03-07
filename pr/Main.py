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

def main():
    print "a*x^2 + b*x + c = 0"
    print "Enter the coefficients for the quadratic equation"

    a = input_param('a')
    b = input_param('b')
    c = input_param('c')

    d = get_discr(a, b, c)

    if d < 0:
        print "Rootis doesn`t exist"
    else:
        x1 = get_eq_root(a, b, d)
        x2 = get_eq_root(a, b, d, order=2)
        if x1 == x2:
            print "There is not root x = %g" % x1
        else:
            print "Trere are roots x1 = %g, x2 = %g" % (x1, x2)

main()