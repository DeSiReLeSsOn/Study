def two_sum(a,b):
    d = ListNode()
    curr_node = d 
    carry = 0 
    while a or b:
        x = a.val if a else 0
        y = b.val if b else 0
        curr_sum = carry + x + y 
        carry = curr_sum // 10 
        curr_node.next = ListNode(curr_sum%10) 
        curr_node = curr_node.next 
        if a:
            a.next 
        if b:
            b.next 
        if carry != 0:
            curr_node.next = ListNode(carry) 
    return d.next  
