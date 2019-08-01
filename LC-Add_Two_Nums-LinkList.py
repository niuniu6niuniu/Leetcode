# You are given two non-empty linked lists representing two non-negative integers.
# The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.
# You may assume the two numbers do not contain any leading zero,
# except the number 0 itself.

# Example:
# Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 0 -> 8
# Explanation: 342 + 465 = 807.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Solution 1: ------ List ------
# [I]. Convert linked list to array
# [II]. Set each element in right format and add them together
# [III]. Combine the two sum and convert it back to array
# [IV]. Reverse the array and make it back to linked list

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        num1 = []
        while l1 is not None:
            num1.append(l1.val)
            l1 = l1.next

        num2 = []
        while l2 is not None:
            num2.append(l2.val)
            l2 = l2.next

        n1 = 0
        n2 = 0
        for i in range(len(num1)):
            n1 += num1[i]*10**i
        for k in range(len(num2)):
            n2 += num2[k]*10**k
            
        n3 = n1 + n2
        snum = str(n3)
        fnum = []
        for s in snum:
            fnum.append(int(s))
        fn = []
        for i in range(len(snum)):
            fn.append(fnum[len(snum)-1-i])
        return fn
    
    
# Solution 2: ------ Recursive -------
# Define a function: 2 linked list, carry(1 or 0), rootNode(store the head), 
# currNode(do iteration over the list) 

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        return addTwoNodes(l1, l2, 0, None, None)

    def addTwoNodes(self, l1, l2, carry, rootNode, currNode):
        if l1 or l2 or carry != 0:
            # Add nodes if they exists
            sum = (l1.val if l1 else 0) + (l2.val if l2 else 0)

            # if current node exists
            if currNode:
                # Assign single digit to next node
                currNode.next = ListNode(sum % 10)
                # Swap current node with the next node
                currNode = currNode.next

            else:
                currNode = ListNode(sum % 10)
                # Reserve the head node
                rootNode = currNode
            return self.addTwoNodes(l1.next if l1 else None, l2.next if l2 else None,
            (sum // 10), rootNode, currNode)
        else:
            return rootNode
