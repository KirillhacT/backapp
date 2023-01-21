
# nums = [3,1,2,10,1]
# N = len(nums)
# one = nums[0]
# new_nums = [one] + [0] * (N-1)
# for i in range(1, N):
#     new_nums[i] = new_nums[i-1] + nums[i]
# print(new_nums)

# text = "a  b c d"
# massive_text = text.split(" ")
# new_str = ""
# for i in massive_text:
#     word = i[::-1]
#     new_str += f"{word} "
# print(new_str.strip())

# def two_sum(nums, target):
#     for i in range(len(nums)):
#         for j in range(len(nums)):
#             if nums[i] + nums[j] == target and i != j:
#                 return [i, j]
#
# print(two_sum([2, 7, 11, 15], 9))

# s = input()
# hash = {}
# for i in s:
#     if i not in hash:
#         hash[i] = 1
#     else:
#         hash[i] += 1
# count = 0
# new_hash = {}
# max_count = 0
# for i in hash:
#     current = hash[i]
#     if current % 2 == 0:
#         count += current
#     else:
#         new_hash[i] = current
#         if current > max_count:
#             max_count = current
# count += max_count
# print(count, new_hash)
























