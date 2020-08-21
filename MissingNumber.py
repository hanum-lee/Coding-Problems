# Restriction
#   linear runtime complexity
#   constant extra space complexity
class Solution:
    def missingNumber(self, nums: [int]) -> int:
        nums.sort()

        for i in range(1,len(nums)):
            expected = nums[i-1] + 1
            if nums[i] != expected:
                return i


print(Solution().missingNumber([9,6,4,2,3,5,7,0,1]))