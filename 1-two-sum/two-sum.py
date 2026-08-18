class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        nummap={}
        for i in range(len(nums)):
            k=target-nums[i]
            if k in nummap:
               return [nummap[k],i]
            else:
                nummap[nums[i]]=i
