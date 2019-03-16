def is_leap_year(y):
    return y % 400 == 0 or y % 100 != 0 and y % 4 == 0

try:
    year = int(input())
    print(is_leap_year(year))
except Exception as err:
    print(err)
