class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq_map, max_heap, interval_count = {}, [], 0

        for char in tasks:
            freq_map[char] = freq_map.get(char, 0) + 1

        # Add all tasks to the max heap
        for char, frequency in freq_map.items():
            heappush(max_heap, [-frequency, char])

        while max_heap:
            wait_list = []
            k = n + 1  # Try to execute as many as 'n + 1' tasks from the max-heap
            while max_heap and k > 0:
                interval_count += 1
                frequency, char = heappop(max_heap)
                if -frequency > 1:
                    # Decrement the frequency and add to the wait_list
                    wait_list.append([frequency + 1, char])
                k -= 1

            # Put all the waiting list back on the heap
            for frequency, char in wait_list:
                heappush(max_heap, [frequency, char])

            if max_heap:
                interval_count += k # We'll be having 'n' idle intervals for the next iteration

        return interval_count

# Time Complexity: The time complexity of the above algorithm is O(N*logN)
# where ‘N’ is the number of tasks. Our while loop will iterate once for
# each occurrence of the task in the input (i.e. ‘N’) and in each iteration
# we will remove a task from the heap which will take O(logN) time. Hence
# the overall time complexity of our algorithm is O(N*logN).

# Space Complexity: The space complexity will be O(N), as in the
# worst case, we need to store all the ‘N’ tasks in the HashMap.