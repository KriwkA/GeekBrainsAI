def check(sum, n):
    return sum == ((n * (n + 1)) // 2)

try:
    sum = 0
    for i in range(1, 1000000):
        sum += i
        if not check(sum, i):
            raise ValueError("{0} != {1}({1}+1)/2".format(sum, i))
    print("Proven on range 1..1'000'000")
except Exception as err:
    print(err)
