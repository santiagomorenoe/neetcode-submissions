class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        h = {}

        if not nums: 
            return 

        for i, num in enumerate(nums): 
            complemento = target - num
            if complemento in h: 
                return [h[complemento], i]
            h[num] = i