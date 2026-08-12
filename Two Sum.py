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

class Solution2:
    def twoSum(self, nums:list[int], target:int) -> list[int]:
        hashmap = {}
        for i in range(len(nums)):
            hashmap[nums[i]] = i
        for i in range(len(nums)):
            if target-nums[i] in hashmap and hashmap[target-nums[i]] != i:
                return [i, hashmap[target-nums[i]]]
        return []

class Solution3:
    def twoSum(self, nums:list[int], target:int) -> list[int]:
        hashmap = {}
        for i in range(len(nums)):
            if target-nums[i] in hashmap:
                return [i, hashmap[target-nums[i]]]
            hashmap[nums[i]] = i
        return []