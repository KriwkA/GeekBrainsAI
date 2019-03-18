import random

val = random.randint(0, 100)

win = False
for i in range(10):
    curr = int(input("Guess the number:"))
    if curr == val:
        print("You Win!")
        win = True
        break
    elif curr > val:
        print("Less")
    else:
        print("More")
if not win:
    print("You lose")
