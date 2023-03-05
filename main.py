def TwoSum( nums , target):
  start = 0
  final = len(nums)-1
  nums.sort()

  while start < final:
    if nums[start] + nums[final] > target:
      final -= 1
    elif nums[start] + nums[final] < target: 
      start += 1
    elif nums[start] + nums[final] == target:
      return True 

  return False 
  
print(TwoSum([1,2,3,4,6], 10))
