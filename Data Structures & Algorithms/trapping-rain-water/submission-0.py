class Solution:
    def trap(self, height: List[int]) -> int:
        largest = 0
        units1 = []
        units2 = []
        total = 0
        # left to right
        for i, h in enumerate(height):
            if h >= largest:
                largest = h
            units1.append(largest)
        # right to left
        largest = 0
        for i, h in enumerate(reversed(height)):
            if h >= largest:
                largest = h
            units2.append(largest)
        for i, j in zip(units1, reversed(units2)):
            total += min(i, j)
        total -= sum(height)
        return total