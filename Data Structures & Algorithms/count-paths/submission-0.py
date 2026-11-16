class Solution(object):
    cache = {}
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        if m == 1 or n == 1:
            return 1
        if (m, n) in self.cache:
            return self.cache[(m, n)]
        down = self.uniquePaths(m-1, n)
        right = self.uniquePaths(m, n-1)
        self.cache[(m, n)] = down+right
        return down+right