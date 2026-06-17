class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i, iv in enumerate(nums):
            for j, jv in enumerate(nums):
                if (iv + jv == target) and (i != j):
                    return [i, j]
            