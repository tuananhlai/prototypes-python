def get_odds():
    for x in range(10):
        if x %2 == 1:
            yield x
count = 1
for number in get_odds():
    if count == 3:
        print(number)
        break
    count += 1