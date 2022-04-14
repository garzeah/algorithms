def reverse_every_k_elements(head, k):
    if k <= 1 or head is None:
        return head

    prev, curr = None, head
    while curr:
        # We are interested in three parts of the LinkedList, the part before index start of kth-group,
        # the part between the kth group, and the part after kth group
        last_node_of_pre_sub_list = prev

        # After reversing the LinkedList 'curr' will become the last node of the sub-list
        last_node_of_sub_list = curr
        i = 0

        # Reverse nodes within the kth group
        while curr and i < k: # Reverse 'k' nodes
            temp_next = curr.next # Temporarily store the next node
            curr.next = prev # Reverse the current node
            prev = curr # Before we move to the next node, point previous to the current node
            curr = temp_next # Move on the next node
            i += 1

        # Connect with pre_sub_list
        if last_node_of_pre_sub_list:
            # Since we reversed, prev will point to the first node in the reversed sub-list
            last_node_of_pre_sub_list.next = prev
        else:
            # Since we reversed, curr will point to the first node post sub-list
            head = prev

        # Connect with the current next sub list
        last_node_of_sub_list.next = curr

        # Getting ready to reverse the upcoming k-group
        prev = last_node_of_sub_list

    return head

# Time Complexity: O(n)
# Space Complexity: O(1)