class Solution:
    def missingInteger(self, nums:list[int]) -> int:
        i = 0
        prefix_sum = nums[0]
        while i < (len(nums)-1) and (nums[i+1] == nums[i] + 1):
            prefix_sum += nums[i+1]
            i += 1
        missing_int = prefix_sum
        while missing_int in nums:
            missing_int += 1

        return missing_int