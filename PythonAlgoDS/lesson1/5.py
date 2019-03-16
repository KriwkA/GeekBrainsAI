try:
    a = input('Input first char:')
    b = input('Input second char:')

    if not(len(a) == 1 or len(b) == 1):
        raise ValueError('len of a and b must be 1')

    if not(a.isalpha() and b.isalpha()):
        raise ValueError('a and b must be alphabetic character')

    a = ord(a.lower()[0])
    b = ord(b.lower()[0])

    alphabetic_start = ord('a')

    print('Pos of first char is:', a - alphabetic_start + 1)
    print('Pos of second char is:', b - alphabetic_start + 1)

    if b < a:
        a, b = b, a

    if a == b:
        print('0 chars between first and second characters')
    else:
        print(b - a - 1, 'chars between first and second characters')

except Exception as err:
    print(err)
