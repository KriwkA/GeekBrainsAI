def sum_of_digits(n):
    sum = 0
    while n != 0:
        sum += n % 10
        n //= 10
    return sum

values = set(map(int, input().split()))


max, max_sum = None, float('-inf')

for val in values:
    cur_sum = sum_of_digits(val)
    if cur_sum > max_sum:
        max_sum = cur_sum
        max = val

print(max, max_sum)
