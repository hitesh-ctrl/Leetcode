class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        nummap = {}
         
        for i in range(len(nums)):
            comp = target-nums[i]
            if (comp in nummap):
                return [i,nummap[comp]]
            nummap[nums[i]] = i
