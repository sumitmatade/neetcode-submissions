class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        values = []

        # Collect all values
        for head in lists:
            while head:
                values.append(head.val)
                head = head.next

        # If no nodes exist
        if not values:
            return None

        # Sort the values
        values.sort()

        # Create new linked list
        dummy = ListNode(0)
        current = dummy

        for val in values:
            current.next = ListNode(val)
            current = current.next

        return dummy.next