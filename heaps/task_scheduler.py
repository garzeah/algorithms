class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
    # Want numbers with the highest freq at the top
        freq_map, heap = Counter(tasks), []

        for freq in freq_map.values():
            heappush(heap, -freq)

        # Queue will contain pairs of [-freq, time until it can run again]
        queue, time = deque(), 0

        # Getting the minimum amount of idle time necessary
        while heap or queue:
            time += 1

            # If we have a value in our heap, we want to get the freq
            # and if it is not 0 then we want to add it into our queue and
            # use it to determine when we can use this task again
            if heap:
                freq = 1 + heappop(heap)
                if freq:
                    queue.append([freq, time + n])

            # We can run this task again
            if queue and queue[0][1] == time:
                heappush(heap, queue.popleft()[0])

        return time

# Time Complexity: O(n), worst case it'd be O(n)*log(26) but that simplifies to O(n)
# Space Complexity: O(n)