class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        indices = [0, 0]
        for i, v in enumerate(nums):
            indices[0] = i
            for j, w in enumerate(nums[i+1:]):
                if v + w == target:
                    indices[1] = j+i+1
                    return indices
        return []