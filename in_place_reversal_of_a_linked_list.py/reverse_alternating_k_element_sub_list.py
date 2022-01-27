def reverse_alternate_k_elements(head, k):
    if k <= 1 or head is None:
        return head

    curr, prev = head, None
    while curr: # Break if we've reached the end of the list
        # We are interested in three parts of the LinkedList, the part before index start of kth-group,
        # the part between the kth group, and the part after kth group
        last_node_of_pre_sub_list = prev

        # After reversing the LinkedList 'curr' will become the last node of the sub-list
        last_node_of_sub_list = curr
        next = None  # will be used to temporarily store the next node

        i = 0
        # Reverse nodes within the kth group
        # curr will end at the first value at the end of the sublist
        # prev will be at the start of the reversed portion
        while curr and i < k:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
            i += 1

        # Connect with the current next sub list
        if last_node_of_pre_sub_list:
            last_node_of_pre_sub_list.next = prev
        else:
            head = prev

        # Getting ready to reverse the upcoming k-group
        last_node_of_sub_list.next = curr

        # skip 'k' nodes
        i = 0
        while curr and i < k:
            prev = curr
            curr = curr.next
            i += 1

    return head