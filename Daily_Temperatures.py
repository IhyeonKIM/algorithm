# https://leetcode.com/problems/daily-temperatures/

# 매일의 온도를 나타내는 int형 배열 temperatures가 주어짐. 
# answer배열의 원소 answer[i]는 i번째 날의 온도보다 더 따뜻해지기까지 며칠을 기다려야하는지 나타낸다.
# 만약 더 따뜻해지는 날이 없다면 0임 
# answer 배열을 반환하는 함수를 구현하시오. 

# O(n), O(nlogn) 정도의 시간복잡도를 요구하는 문제 

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        ans = [0] * len(temperatures)
        for cur_day, temp in enumerate(temperatures): 
            while stack and stack[-1][1] < temp :
                prev_day,_ = stack.pop() 
                ans[prev_day] = cur_day - prev_day 
            stack.append((cur_day,temp)) 

        return ans 


