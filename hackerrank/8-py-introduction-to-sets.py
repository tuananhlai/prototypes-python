def average(arr):
    # your code goes here
    distinct_heights = set(arr)
    sum_heights = sum(distinct_heights)
    count = len(distinct_heights)
    return sum_heights / count
    
if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)