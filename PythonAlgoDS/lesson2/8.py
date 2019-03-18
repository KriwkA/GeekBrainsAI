try:
    input_str = input().split()
    n = int(input_str[0])

    if n < 1 or len(input_str[1]) != 1:
        raise ValueError("Invalid input")

    check_digit = input_str[1][0]

    count = 0
    for i in range(0, n):
        val = int(input())
        count += str(val).count(check_digit)

    print("Count of digit {0} is {1}".format(check_digit, count))

except Exception as err:
    print(err)
