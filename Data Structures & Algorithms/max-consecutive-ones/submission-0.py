class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        consecutivos, maximos = 0,0

        for n in nums:
            if n == 1:
                consecutivos += 1 
                if consecutivos > maximos:
                    maximos += 1
            else: 
                consecutivos = 0 

        return maximos 

         
        