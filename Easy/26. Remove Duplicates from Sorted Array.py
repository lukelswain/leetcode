class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        pointerleft = 0
        pointerright = 1
        while pointerright < len(nums):
            if nums[pointerright] == nums[pointerleft]:
                del nums[pointerright]
                continue
            pointerleft += 1
            pointerright += 1
        return len(nums)

class Solution2:
    def removeDuplicates(self, nums:list[int]) -> int:
        j = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[i-1]:
                nums[j] = nums[i]
                j += 1
        return j