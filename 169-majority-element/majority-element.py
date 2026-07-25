class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nummap = {}
        for i in range(len(nums)):
            if nums[i] in nummap:
                nummap[nums[i]]+=1
            else:
                nummap[nums[i]]=1
        
        return max(nummap , key= nummap.get)
