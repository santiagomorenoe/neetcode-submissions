class Solution:
    def majorityElement(self, nums: List[int]) -> int:
       counts = {}
       mayorityCount = len(nums) // 2
       
       for n in nums:
        counts[n] = counts.get(n, 0) + 1
        if counts[n] > mayorityCount:
            return n