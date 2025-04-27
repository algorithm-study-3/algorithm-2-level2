nums = list(map(int, input().split()))
operator = ['+', '-', '*', '/']

for i in range(4):
    res = str(nums[1]) + operator[i] + str(nums[2])
    if eval(res) == nums[0]:
        print(str(nums[0]) + '=' + res)
        exit(0)

for i in range(4):
    res = str(nums[0]) + operator[i] + str(nums[1])
    if eval(res) == nums[2]:
        print(res + '=' + str(nums[2]))
        exit(0)