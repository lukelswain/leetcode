# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:
        pointer1 = list1
        pointer2 = list2
        newlist = None
        newcurrent = None
        if list1 is None:
            return list2
        if list2 is None:
            return list1
        if list1.val < list2.val:
            newlist = list1
            pointer1 = pointer1.next
        else:
            newlist = list2
            pointer2 = pointer2.next
        newcurrent = newlist
        while pointer1 is not None and pointer2 is not None:
            if pointer1.val < pointer2.val:
                newcurrent.next = pointer1
                newcurrent = newcurrent.next
                pointer1 = pointer1.next
            else:
                newcurrent.next = pointer2
                newcurrent = newcurrent.next
                pointer2 = pointer2.next
        if pointer1 is None:
            while pointer2 is not None:
                newcurrent.next = pointer2
                newcurrent = newcurrent.next
                pointer2 = pointer2.next
            return newlist
        if pointer2 is None:
            while pointer1 is not None:
                newcurrent.next = pointer1
                newcurrent = newcurrent.next
                pointer1 = pointer1.next
            return newlist