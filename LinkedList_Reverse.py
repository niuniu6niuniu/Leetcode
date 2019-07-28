# Define Linked List
class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

# 3 boxes
    def Fun1(head):
        p = head        # Use p to store the head
        q = p.next      # Use q to store the value of p.next
        p.next = None   # Set p.next points to None (pto the last place)
        while q:
            r = q.next  # Use r to store value of q.next (p.next.next)
            q.next = p  # Set q.next points to p (q to the second last place)
            p = q       # Move p forward
            q = r       # Move q forward
        return p

# Solution (2):
