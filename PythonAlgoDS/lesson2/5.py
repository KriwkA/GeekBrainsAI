row = '| '
for i in range(32, 128):
    row += '{0:>3}: {1} | '.format(i, chr(i))
    if (i - 1) % 10 == 0 or i == 127:
        print(row)
        row = '| '

