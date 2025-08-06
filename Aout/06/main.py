from typing import List, Optional


class TreeNode:
    def __init__(
        self,
        val: int = 0,
        left: Optional["TreeNode"] = None,
        right: Optional["TreeNode"] = None,
        mother: Optional["TreeNode"] = None,
    ) -> None:
        self.val = val
        self.left = left
        self.right = right
        self.mother = mother


class SegmentTree:
    def __init__(self, li: List[int]) -> None:
        self.root = self.build_tree(li)

    def build_tree(self, li: List[int]) -> Optional[TreeNode]:
        if not li:
            return None

        if len(li) == 1:
            return TreeNode(li[0])

        root = TreeNode()
        i = len(li) // 2
        root.left = self.build_tree(li[:i])
        root.right = self.build_tree(li[i:])

        l_val = root.left.val if root.left else 0
        r_val = root.right.val if root.right else 0
        root.val = max(l_val, r_val)

        if root.left:
            root.left.mother = root
        if root.right:
            root.right.mother = root

        return root

    def get(self, root: Optional[TreeNode], leftmost: int) -> Optional[TreeNode]:
        if not root or root.val < leftmost:
            return None

        if not root.left and not root.right:
            return root

        if root.left and root.left.val >= leftmost:
            return self.get(root.left, leftmost)
        else:
            return self.get(root.right, leftmost)

    def update(self, leftmost: int) -> bool:
        node = self.get(self.root, leftmost)
        if not node:
            return False

        node.val = 0
        while node.mother:
            node = node.mother
            l_val = node.left.val if node.left else 0
            r_val = node.right.val if node.right else 0
            node.val = max(l_val, r_val)

        return True


class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        st = SegmentTree(baskets)
        ans = 0
        for f in fruits:
            if not st.update(f):
                ans += 1

        return ans
    
    
solution = Solution()
fruits = [4,2,5]
baskets = [3,5,4]
print(solution.numOfUnplacedFruits(fruits, baskets))