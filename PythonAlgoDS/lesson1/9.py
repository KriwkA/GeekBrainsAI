try:
    a = [int(input()), int(input()), int(input())]
    a.sort()
    print(a[1])
except Exception as err:
    print(err)
