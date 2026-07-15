class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        #hashset data structure 
        hset = set()

        for n in nums:
            if n in hset:
                return True
            hset.add(n)
        return False

        # space complexity: O(n)
        # time complexity: O(n)