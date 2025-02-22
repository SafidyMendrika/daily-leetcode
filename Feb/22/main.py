class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
    def __str__(self):
        return self._get_tree_str()
    
    def _get_tree_str(self, level=0, prefix="Root: "):
        ret = "  " * level + prefix + str(self.val) + "\n"
        if self.left:
            ret += self.left._get_tree_str(level + 1, "L--- ")
        if self.right:
            ret += self.right._get_tree_str(level + 1, "R--- ")
        return ret


class Solution(object):
    def recoverFromPreorder(self, traversal):
        stack = []
        i = 0
        
        while i < len(traversal):
            level = 0
            while i < len(traversal) and traversal[i] == '-':
                level += 1
                i += 1
            
            value = 0
            while i < len(traversal) and traversal[i].isdigit():
                value = value * 10 + int(traversal[i])
                i += 1
            
            node = TreeNode(value)
            
            while len(stack) > level:
                stack.pop()
            
            if stack:
                if not stack[-1].left:
                    stack[-1].left = node
                else:
                    stack[-1].right = node
            
            stack.append(node)
        
        return stack[0]


traversal = "1-2--3--4-5--6--7"
s = Solution()
print(s.recoverFromPreorder(traversal))