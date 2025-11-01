from typing import List, Optional

class ListNode : 
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def print(self) : 
        print(f"{self.val} -> ")
        if self.next : 
            self.next.print()

class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        to_delete = set(nums)
        
        dummy = ListNode(0, head)
        prev, curr = dummy, head
        
        while curr:
            if curr.val in to_delete:
                prev.next = curr.next
            else:
                prev = curr
            curr = curr.next
        
        return dummy.next
    

solution = Solution()    
nums = [1]
head = ListNode(1,ListNode(2,ListNode(1,ListNode(2,ListNode(1,ListNode(2))))))

r = solution.modifiedList(nums,head)
r.print()