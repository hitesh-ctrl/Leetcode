class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        s= set(nums)
        longest = 0
        for num in s:
            if num-1 not in s:
                next_num = num+1
                length =1
                while next_num in s:
                    next_num+=1
                    length+=1
                longest=max(longest, length)
        return longest