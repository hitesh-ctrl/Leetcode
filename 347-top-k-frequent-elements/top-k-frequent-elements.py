class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        nummap={}
        for i in nums:
            if i in nummap:
                nummap[i]+=1
            else:
                nummap[i] =1
        
        
        keys = sorted(nummap, key = nummap.get,reverse=True)
        return keys[:k]
        