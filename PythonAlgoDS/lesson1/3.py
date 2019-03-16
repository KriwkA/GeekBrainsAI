eps = 0.0001

x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())

try:
    if x1 == x2:
        raise ValueError('Can`t make linear equation from two points with same argument X')

    k = (y1 - y2) / (x1 - x2)
    b = y1 - x1 * k

    if y1 == y2:
        print('y = b')
    elif abs(b) > eps:
        if b > 0:
            print('y =', k, '* x +', b)
        else:
            print('y =', k, '* x -', -b)
    elif abs(k - 1.0) > eps:
        print('y =', k, '* x')
    else:
        print('y = x')

except Exception as err:
    print(err)
