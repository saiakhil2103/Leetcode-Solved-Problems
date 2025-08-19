# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        len1=0
        temp=headA
        while temp:
            len1+=1
            temp=temp.next
        len2=0
        temp=headB
        while temp:
            len2+=1
            temp=temp.next
        if len1>=len2:
            for _ in range(len1-len2):
                headA=headA.next
        else:
            for _ in range(len2-len1):
                headB=headB.next
        while headA and headB:
            if headA==headB:
                return headA
            headA=headA.next
            headB=headB.next
        return None
