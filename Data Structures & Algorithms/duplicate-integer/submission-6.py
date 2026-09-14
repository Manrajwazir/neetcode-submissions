class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        holder = []
        for num in nums:
            if num in holder:
                return True
            holder.append(num)
        return False

        