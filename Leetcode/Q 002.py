# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        N, i = 0, 1
        while (l1 != None):
            N += (l1.val)*i
            l1 = l1.next
            i*=10
        i = 1
        while (l2 != None):
            N += (l2.val)*i
            l2 = l2.next
            i*=10
        resultado = ListNode(N%10)
        N = N//10
        noAtual = resultado
        while(N > 0):
            noAtual.next = ListNode(N%10)
            N = N//10
            noAtual = noAtual.next
        return resultado