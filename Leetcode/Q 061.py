# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if (head == None):
            return head
        inicio = head
        final = head
        tamanho = 1
        while(final.next != None):
            final = final.next
            tamanho+=1
        final.next = inicio
        for i in range(0, tamanho-(k%tamanho)):
            inicio = inicio.next
            final = final.next
        final.next = None
        return inicio