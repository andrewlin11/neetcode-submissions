class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ints = []
        nums = sorted(nums)
        for i, num in enumerate(nums):
            l = i + 1
            r = len(nums) - 1

            if (i > 0) and (num == nums[i - 1]):
                continue

            while l < r:
                sum = nums[l] + nums[r] + num
                if sum == 0:
                    ints.append([nums[l], nums[r], num])
                    l += 1
                    r -= 1
                    while (nums[l] == nums[l - 1]) and (l < r):
                        l += 1    
                    while (nums[r] == nums[r + 1]) and (l < r):
                        r -= 1
                elif sum < 0:
                    l += 1
                else:
                    r -= 1
        return ints