class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxarea = 0
        l = 0
        r = len(heights) - 1
        while l < r:
            curarea = (r - l) * min(heights[l], heights[r])
            maxarea = max(maxarea, curarea)
            
            if heights[r] > heights[l]:
                l += 1
            else:
                r -= 1
        return maxarea