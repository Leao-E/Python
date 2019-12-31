# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if (head == None):
            return head
        atual = head.next
        anterior = head
        while (atual != None):
            if(anterior.val == atual.val):
                anterior.next = atual.next
                atual = atual.next
            else:
                anterior = anterior.next
                atual = atual.next
        return head