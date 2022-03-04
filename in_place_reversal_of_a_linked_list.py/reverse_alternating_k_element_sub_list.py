def reverse_alternate_k_elements(head, k):
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
        while curr and i < k:
            temp_next = curr.next # Temporarily store the next node
            curr.next = prev # Reverse the current node
            prev = curr # Before we move to the next node, point previous to the current node
            curr = temp_next # Move on the next node
            i += 1

        # Connect with the current next sub list
        if last_node_of_pre_sub_list:
            last_node_of_pre_sub_list.next = prev
        else:
            head = prev

        # Getting ready to reverse the upcoming k-group
        last_node_of_sub_list.next = curr

        # Skip 'k' nodes
        i = 0
        while curr and i < k:
            prev = curr # Prev should be the first node of reversed but this helps it catch up
            curr = curr.next
            i += 1

    return head