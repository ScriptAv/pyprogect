from qudr.utilits import get_discr, get_eq_root, input_param
#from utilits import * #!!*
#import utilits
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

if __name__ == "__main__":
    main()