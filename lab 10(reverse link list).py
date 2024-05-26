class Solution(object):
    def reverseList(self, head):
        prev = None  # Initialize a pointer to None. This will eventually become the new tail of the list.
        curr = head  # Initialize another pointer to the head of the list, to start traversing the list.
        
        # Loop until curr is None, which means we've reached the end of the list.
        while curr:
            next_node = curr.next  # Store the next node temporarily since we're about to change curr.next.
            curr.next = prev  # Reverse the link: point the current node's next pointer to the previous node.
            prev = curr  # Move the prev pointer forward: it now points to the current node.
            curr = next_node  # Move the curr pointer forward: it now points to the next node in the original list.
        
        # At the end of the loop, curr is None (we've reached the end of the list),
        # and prev is the last node we processed, which is the new head of the reversed list.
        return prev  # Return the new head of the reversed list.
    # Definition for singly-linked list.
# class ListNode(object):
# def __init__(self, val=0, next=None):
# self.val = val
# self.next = next

class Solution(object):
    def mergeTwoLists(self, list1, list2):
        # Initialize a dummy node with value -1.
        # This dummy node serves as the head of the merged list.
        dummy = ListNode (-1)
        # Initialize a pointer 'current' to the dummy node.
        # 'current' will be used to build the merged list.
        current = dummy
        # Loop until both list1 and list2 have nodes to merge.
        while list1 and list2:
            # Compare the values of the current nodes in list1 and list2.
            if list1.val < list2.val:
                # If the value of the current node in list1 is smaller,
                # attach it to 'current.next'.
                current.next = list1
                # Move the pointer of list1 to its next node.
                list1 = list1.next
            else:
                # If the value of the current node in list2 is smaller or equal,
                # attach it to 'current.next'.
                current.next = list2
                # Move the pointer of list2 to its next node.
                list2 = list2.next
            # Move the 'current' pointer to the next node in the merged list.
            current = current.next
        # If list1 still has remaining nodes, attach them to the end of the merged list.
        if list1:
            current.next = list1
        # If list2 still has remaining nodes, attach them to the end of the merged list.
        elif list2:
            current.next = list2
        # Return the head of the merged list, which is the next node after the dummy node.
        return dummy.next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        # Initialize a dummy node with value 0 and point its next to the head of the original list.
        dummy = ListNode(0, head)
        # Initialize two pointers 'slow' and 'fast' to the dummy node.
        # Both pointers will be used to find the node to be removed.
        slow = fast = dummy
        # Move the 'fast' pointer n steps ahead of the 'slow' pointer.
        for i in range(n):
            fast = fast.next
        # Move both 'slow' and 'fast' pointers until 'fast' reaches the last node.
        # At this point, 'slow' will be pointing to the node before the one to be removed.
        while fast.next:
            slow = slow.next
            fast = fast.next
        # Remove the Nth node from the end by updating 'slow.next' to skip the next node.
        slow.next = slow.next.next
        # Return the head of the modified list (next node after the dummy node).
        return dummy.next