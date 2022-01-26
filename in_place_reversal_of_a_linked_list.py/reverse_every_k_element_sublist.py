def reverse_every_k_elements(head, k):
  curr, prev = head, None

  while True:
    # We are interested in three parts of the LinkedList, the part before index start of kth-group,
    # the part between the kth group, and the part after kth group
    last_node_of_pre_sub_list = prev

    # After reversing the LinkedList 'curr' will become the last node of the sub-list
    last_node_of_sub_list = curr
    i = 0

    # Reverse nodes within the kth group
    # curr will end at the first value at the end of the sublist
    # prev will be at the start of the reversed portion
    while curr and i < k: # Reverse 'k' nodes
      next = curr.next
      curr.next = prev
      prev = curr
      curr = next
      i += 1

    print(prev.value)

    # Connect with pre_sub_list
    if last_node_of_pre_sub_list:
      last_node_of_pre_sub_list.next = prev
    else:
      head = prev

    # Connect with the current next sub list
    last_node_of_sub_list.next = curr

    if curr is None:
      break

    # Getting ready to reverse the upcoming k-group
    prev = last_node_of_sub_list

  return head

# Time Complexity: O(n)
# Space Complexity: O(1)