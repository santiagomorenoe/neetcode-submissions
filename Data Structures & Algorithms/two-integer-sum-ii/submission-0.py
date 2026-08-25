class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers) - 1

        while left < right:
            acc = numbers[left] + numbers[right]
            if acc == target:
                return [left+1, right+1]
            elif acc < target: 
                left += 1
            elif acc > target:
                right -= 1

        