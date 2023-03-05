## 1.완전 탐색
def TwoSum(nums, target):
  for i in range(len(nums)):
    for j in range(len(nums)):
      if nums[i] + nums[j] == target:
        return True
  return False


print(TwoSum(nums = [1, 2, 3, 4, 6], target = 10))