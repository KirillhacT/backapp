
with open("27-A_demo.txt") as file:
    data = file.read()

nums = data.split("\n")
if nums[-1] == "":
    nums = nums[:-1]

sum = 0
d = 10**6
N = int(nums[0])
for i in range(1, N):
    string = list(map(int, nums[i].split("  ")))
    num1 = string[0]
    num2 = string[1]
    sum += max(num1, num2)

    salt = abs(num1 - num2)
    if salt % 3 != 0:
        d = min(d, salt)

if sum % 3 != 0:
    print(sum)
else:
    print(sum - d)



