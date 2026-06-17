class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        products = []
        temp = 1
        for i in range(len(nums)):
            if i == 0:
                products.append(1)
                continue
            else:
                temp *= nums[i-1]
                products.append(temp)
        temp = 1
        for i in range(len(nums) - 1, -1, -1):
            products[i] *= (temp)
            temp *= nums[i]
        return products
        
