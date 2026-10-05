from ListNode import ListNode

class Solution:
    def mergeTwoLists(self, list1: ListNode | None, list2: ListNode | None) -> ListNode | None:
        head = ListNode(0)
        atual = head
        
        while list1 and list2:
            if list1.val <= list2.val:
                atual.next = list1
                list1 = list1.next
            else:
                atual.next = list2
                list2 = list2.next
            atual = atual.next
            
        atual.next = list1 if list1 else list2
        return head.next
        
        