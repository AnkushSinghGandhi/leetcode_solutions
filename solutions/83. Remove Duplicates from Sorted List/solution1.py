from typing import Optional

class ListNode:
    def _init_(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = head
        if head:
            while cur.next != None:
                if cur.next:
                    if cur.val == cur.next.val:
                        cur.next = cur.next.next
                    else:
                        cur = cur.next
        return head