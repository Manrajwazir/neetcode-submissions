class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for nums in matrix:
            l = 0
            r = len(nums) - 1

            while l <= r:
                m = l + ((r - l) // 2)

                if nums[m] < target:
                    l = m + 1
                elif nums[m] > target:
                    r = m - 1
                else:
                    return True
        return False