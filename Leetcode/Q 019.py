# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        aux = head
        atual = head
        for i in range(0, n):
            atual = atual.next
        if (atual == None):
            return head.next
        while(atual.next != None):
            atual = atual.next
            aux = aux.next
        aux.next = aux.next.next
        return head