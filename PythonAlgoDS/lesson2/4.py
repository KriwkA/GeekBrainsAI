try:
    n = int(input())
    sum = 0.0
    for i in range(n):
       sum += float(input())
    print(sum)

except Exception as err:
    print(err)
