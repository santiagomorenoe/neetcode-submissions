class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        ordenada = sorted(nums)
        for i,n in enumerate(ordenada):
            if i != ordenada[i]:
                return i
        return len(ordenada)
        