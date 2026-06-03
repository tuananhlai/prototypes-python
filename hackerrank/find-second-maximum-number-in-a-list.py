if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    max_val = arr[0]
    second_largest_val = -100
    for x in arr:
        if x > max_val:
            second_largest_val = max_val
            max_val = x
        elif x > second_largest_val and x < max_val:
            second_largest_val = x

    print(second_largest_val)