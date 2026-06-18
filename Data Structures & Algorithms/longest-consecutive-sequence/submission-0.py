class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if (len(nums) == 0) or (len(nums) == 1):
            return len(nums)
        setnums = set(nums)
        length = 1
        
        for num in setnums:
            if (num - 1) not in setnums:
                temp = num
                cur = 1
                while (temp + 1) in setnums:
                    temp += 1
                    cur += 1
                length = max(length, cur)

        return length
