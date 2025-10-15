from typing import List

def twoSum(nums: List[int], target: int) -> List[int]:# YOUR ANSWER
    
    for i in nums:
       for j in nums:
           if i + j == target:
               return [i, j] 

    return 0