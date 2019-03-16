import random

try:
    left = int(input())
    right = int(input())

    if left > right:
        left, right = right, left

    print(random.randint(left, right))
    print(random.random() * (right - left) + left)

    left = input()
    right = input()

    if not(len(left) == 1 or len(right) == 1):
        raise ValueError('len of left and right must be 1')

    left = ord(left[0])
    right = ord(right[0])

    if left > right:
        left, right = right, left

    print(chr(random.randint(left, right)))

except Exception as err:
    print(err)

