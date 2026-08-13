"""
# Definition for a Node.
class Node(object):
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        if not node:
            return None

        dict_ = {}
        
        def clone(original):
            if original in dict_:
                return dict_[original]
            newNode = Node(original.val)
            dict_[original] = newNode
            for n in original.neighbors:
                newNode.neighbors.append(clone(n))
            return newNode
        return clone(node)

