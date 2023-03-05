#https://leetcode.com/problems/two-sum/
#Two Sum문제 -> True / False 로 반환 

#문제
#정수가 저장된 배열 nums이 주어졌을 때,nums의 원소중 두 숫자를 더해서 target이 될 수 있으면 T 아니면 F 반환 
#같은 원소를 두번 사용할 수 없음. 

## 1.완전 탐색 

def TwoSum(nums , target ):
  for i in range(len(nums)):
    for j in range(len(nums)-1):
      if nums[i] + nums[j] == target:
        return True
  return False 

print(TwoSum([1,2,3,4,6], 10))


## 2.투포인터

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
