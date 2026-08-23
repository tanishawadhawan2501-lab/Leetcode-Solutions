class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans = 0

        for nums in nums:
            ans= ans^nums
        return ans