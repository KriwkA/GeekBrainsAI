def foo(value):
    if value == 1:
        return [1, 0]
    res = [0, 0]
    while value != 0:
        if value & 1 == 0:
            res[0] += 1
        else:
            res[1] += 1
        value //= 10
    return res


try:
    a = int(input())
    res = foo(a)
    print(res[0], 'odd and', res[1], "even digits")

except Exception as err:
    print(err)
