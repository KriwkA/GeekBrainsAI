try:
    char = int(input('Input char pos:'))
    count = ord('z') - ord('a') + 1

    if char < 1 or char > count:
        raise ValueError('Invalid input char. Out of range.')

    print(chr(char - 1 + ord('a')));

except Exception as err:
    print(err)
