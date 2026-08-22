class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        l=0
        minl = 0
        freq={}
        lettersToSatisfy=len(t)
        left, right = float('-inf'), float("inf")
        i=0
        for c in t:
            if c in freq:
                freq[c]+=1
            else:
                freq[c]=1
        for j, char in enumerate(s):
            if char in freq:
                
                if freq[char]>0:
                    lettersToSatisfy-=1
                freq[char]-=1
            while lettersToSatisfy == 0:
                if j-i < right-left:
                    left,right = i, j
                if s[i] in freq:
                    freq[s[i]]+=1
                    if freq[s[i]]>0:
                        lettersToSatisfy+=1
                i+=1
        return "" if right == float("inf") else s[left:right+1]

        
