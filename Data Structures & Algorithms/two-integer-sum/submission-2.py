class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
      seen = {}
      for i in range(len(nums)):
        num = nums[i]
        d = target - nums[i]
        if d in seen:
            return [seen[d],i]
        seen[num] = i
        

        
        

                
    
        