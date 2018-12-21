# @Time    : 18/4/11 下午4:10
# @Author  : liweiwei1419
# @Site    : http://www.liwei.party/
# @Contact : liweiwei1419@gmail.com


class Solution:

    def _rob_helper(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n == 0:
            return 0

        if n <= 2:
            return max(nums)
        dp = [-1] * 2

        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])

        for i in range(2, n):
            dp[i % 2] = max(nums[i] + dp[(i - 2) % 2], dp[(i - 1) % 2])
        return dp[(n - 1) % 2]


    def rob(self, nums):
        """
        # 转换成原问题去考虑
        :type nums: List[int]
        :rtype: int
        """

        l = len(nums)
        if l == 0:
            return 0
        if l <= 3:
            return max(nums)

        res1 = self._rob_helper(nums[:-1])
        res2 = self._rob_helper(nums[1:])

        return max(res1, res2)
