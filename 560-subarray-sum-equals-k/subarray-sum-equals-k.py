class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        summap = {0:1}
        s=0
        count=0
        for num in nums:
            s+=num
            if s-k in summap:
                count+=summap[s-k]
            if s in summap:
                summap[s]+=1
            else:
                summap[s]=1
        return count

            
        