import re

operations = {
    '+': lambda a, b: a + b,
    '-': lambda a, b: a - b,
    '*': lambda a, b: a * b,
    '/': lambda a, b: a / b
}

print("Expression must be <int value 1><+|-|*|/><int value 2>")
print("Enter 0 for exit")

while True:
    try:
        in_str = input("Enter the expression: ")
        in_str = ''.join(in_str.split())

        if in_str == "0":
            break

        rx_check = re.match('^\\d{1,}[+,-,*,\\/]\\d{1,}$', in_str)
        if not rx_check:
            raise ValueError("invalid input")

        operator = re.search('[+,-,*,\\/]', in_str).group(0)
        args = in_str.split(operator)
        print(operations[operator](int(args[0]), int(args[1])))

    except Exception as err:
        print(err)
