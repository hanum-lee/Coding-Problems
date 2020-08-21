class Solution:
    def singleNumber(self, nums: [int]) -> int:
        if len(nums) == 1:
            return nums[0]
        nums.sort()
        if(nums[len(nums)-1] != nums[len(nums)-2]):
            return nums[len(nums)-1]
        for i in range(0,len(nums)-1,2):
            if nums[i] != nums[i+1]:
                if nums[i+1] == nums[i+2]:
                    return nums[i]
                else:
                    return nums[i+1]

class PossibleSolution:
    # bit wise opperation with XOR
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a = 0
        for i in nums:
            a ^= i
        return a

print(Solution().singleNumber([1]))