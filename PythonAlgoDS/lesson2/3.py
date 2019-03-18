try:
    a = int(input())
    a = str(a)
    a = a[::-1]
    a = int(a)
    print(a)

except Exception as err:
    print(err)
