class Solution(object):
    def countSmaller(self, nums):
        ans = []
        arr = []

        for num in nums[::-1]:
            i = bisect_left(arr,num)
            ans.append(i)
            insort(arr,num)

        return ans[::-1]