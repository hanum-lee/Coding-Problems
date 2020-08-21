class Solution:
    def runningSum(self, nums: [int]) -> [int]:
        sum = 0
        result = []
        for num in nums:
            sum += num
            result.append(sum)
        return result

print(Solution().runningSum([1,2,3,4]))
        