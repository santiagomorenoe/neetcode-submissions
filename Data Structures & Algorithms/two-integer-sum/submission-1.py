class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        h = { }

        if not nums: 
            return 

        for indice, valorActual in enumerate(nums):
            complemento = target - nums[indice]
            if complemento in h:
                return [h[complemento], indice]
            h[valorActual] = indice
        return []
        