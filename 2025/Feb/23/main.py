class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val        
        self.left = left    
        self.right = right    

    def __str__(self):
        return self._to_string_helper(self, 0)
    
    def _to_string_helper(self, node, level):

        if not node:
            return "None"
            
        indent = "  " * level
        result = f"{node.val}\n"
        
        result += f"{indent}L: {self._to_string_helper(node.left, level + 1)}\n"
        result += f"{indent}R: {self._to_string_helper(node.right, level + 1)}"
        
        return result

class Solution(object):
    def constructFromPrePost(self, preorder, postorder):
        if not preorder:
            return None
            
        root = TreeNode(preorder[0])
        
        if len(preorder) == 1:
            return root
            
        left_root = preorder[1]
        left_size = postorder.index(left_root) + 1
        
        root.left = self.constructFromPrePost(
            preorder[1:left_size + 1],  
            postorder[:left_size]       
        )
        
        root.right = self.constructFromPrePost(
            preorder[left_size + 1:],    
            postorder[left_size:-1]      
        )
        
        return root
    
s = Solution()
preorder = [1,2,4,5,3,6,7], 
postorder = [4,5,2,6,7,3,1]
print(s.constructFromPrePost(preorder,postorder))