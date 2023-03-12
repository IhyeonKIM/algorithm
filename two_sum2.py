# https://leetcode.com/problems/two-sum/

# 시간복잡도를 낮추기 위해서 해시함수를 활용(딕셔너리 활용.)

# 전체 시간복잡도 O(n) 

#인프런 강의 기준 구현 


def twoSum(nums, target) -> bool:

    dict = {}

    for num in nums :
      dict[num] = 1
    for num in nums :
      n = target - num 
      if n in dict: # 딕셔너리에서 찾기때문에, 이 코드가 O(1)이 됨. 
          
        return True 

        
    return False 



## 직접 풀어보기 


def twoSum(nums, target) -> bool:

    dict = {}

    for idx, num in enumerate(nums) :
      dict[num] = idx
    for idx, num in enumerate(nums)  :
      n = target - num 
      if n in dict and idx != dict[n]: # 딕셔너리에서 찾기때문에, 이 코드가 O(1)이 됨. 
          
        return True 
    return False 

print(twoSum([3,3], 6))



class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
          
      dict = {}
  
      for idx, num in enumerate(nums) :
        dict[num] = idx
      for idx, num in enumerate(nums)  :
        n = target - num 
        if n in dict and idx != dict[n]:
          return (idx,dict[n]) 