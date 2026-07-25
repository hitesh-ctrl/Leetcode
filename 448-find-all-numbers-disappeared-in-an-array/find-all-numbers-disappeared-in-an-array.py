class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        numset = set(nums)
        dis = []
        for i in range(1,n+1):
            if( i not in numset):
                dis.append(i)
        return dis