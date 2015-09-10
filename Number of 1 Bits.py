__author__ = 'Eame'


class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        mylist = list(str("{0:b}".format(n)))
        return mylist.count('1')

test = Solution()
print(test.hammingWeight(12))
print(test.hammingWeight(7))
