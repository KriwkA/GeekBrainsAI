try:
    val = int(input())
    if val < 100 or val > 999:
        raise ValueError('Input val len != 3')

    sym = [val // 100, val % 100 // 10, val % 10]

    print(sym[0] + sym[1] + sym[2])
    print(sym[0] * sym[1] * sym[2])

except Exception as err:
    print(err)
