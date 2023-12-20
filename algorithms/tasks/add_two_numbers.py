"""You are given two non-empty linked lists representing two non-negative integers. 
The digits are stored in reverse order, and each of their nodes contains a single digit. 
Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.
Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.
Example 2:

Input: l1 = [0], l2 = [0]
Output: [0]
Example 3:

Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def addTwoNumbers(l1: ListNode, l2: ListNode):
        d = ListNode()
        curr_node = d
        carry = 0
        while l1 or l2:
            x = l1.val if l1 else 0
            y = l2.val if l2 else 0
            curr_sum = carry + x + y 
            carry = curr_sum // 10 
            curr_node.next = ListNode(curr_sum % 10)
            curr_node = curr_node.next
            if l1:
                l1 = l1.next 
            if l2:
                l2 = l2.next 
        if carry != 0:
            curr_node.next = ListNode(carry)
        return d.next
        

l1 = ListNode(2)
l1.next = ListNode(4)
l1.next.next = ListNode(3) 
l2 = ListNode(5)
l2.next = ListNode(6)
l2.next.next = ListNode(4) 
result = addTwoNumbers(l1, l2)
while result:
    print(result.val, end=" ")
    result = result.next