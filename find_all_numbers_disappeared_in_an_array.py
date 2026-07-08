class Solution(object):
    def findDisappearedNumbers(self, nums):
        for n in nums:
            nums[abs(n) - 1] = -abs(nums[abs(n) - 1])

        ans = []
        for i in range(len(nums)):
            if nums[i] > 0:
                ans.append(i + 1)

        return ans