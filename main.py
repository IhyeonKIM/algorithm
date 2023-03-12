################
# TEST 용 py 파일 
################


#인프런 기준 
def twoSum(nums, target) -> bool:

    dict = {}

    for idx, num in enumerate(nums) :
      dict[num] = idx
    for idx, num in enumerate(nums)  :
      n = target - num 
      if n in dict and idx != dict[n]:
        return True 
    return False 


print(twoSum([1,2,3,4,6], 10))
print(twoSum([3,3], 6))
print(twoSum([3,3], 7))

#릿코드 기준

def twoSum(nums, target) :
          
  dict = {}
  
  for idx, num in enumerate(nums) :
    dict[num] = idx
  for idx, num in enumerate(nums)  :
    n = target - num 
    if n in dict and idx != dict[n]:
      return (idx,dict[n]) 

print(twoSum([1,2,3,4,6], 10))
print(twoSum([3,3], 6))
