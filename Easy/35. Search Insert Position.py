class Solution:
    def searchInsert(self, nums:list[int], target: int) -> int:
        total_index = 0
        while nums:
            index = len(nums) // 2
            total_index += index
            if nums[index] == target:
                return total_index
            if nums[index] > target:
                total_index -= index
                nums = nums[:index]
                continue
            if nums[index] < target:
                total_index += 1
                nums = nums[index+1:]
                continue
        return total_index

class Solution2:
    def searchInsert(self, nums:list[int], target:int) -> int:
        first = 0
        end = len(nums) - 1
        while first <= end:
            mid = (first + end) // 2
            if nums[mid] == target:
                return mid
            if target < nums[mid]:
                end = mid - 1
            else:
                first = mid + 1
        return first