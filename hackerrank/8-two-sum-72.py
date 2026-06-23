# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
nums = []
for _ in range(n):
    nums.append(int(input()))
target = int(input())
seen = {}
for i in range(len(nums)):
    num = nums[i]
    ans = target - num
    if ans in seen:
        print(seen[ans], i)
        break
    seen[num] = i