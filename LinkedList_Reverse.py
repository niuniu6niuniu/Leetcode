# Linked List Reverse

# Def linked List
class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

    def LinkedList_Reverse(root):
        # Set root as head
        head = root
        # Use body to store head.next
        body = head.next
        # Set head.next to None (Put head to the end of the list)
        head.next = None
        # Iterate through the List
        while body:
            # Use tail to store body.next
            tail = body.next
            # Put body to the place before head(root), second last element
            body.next = head
            # Move head and body one step forward
            head = body
            body = tail
        return head
