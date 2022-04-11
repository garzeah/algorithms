class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq_map, max_heap = Counter(tasks), []

        for count in freq_map.values():
            heappush(max_heap, -count)

        # Queue will contain pairs of [-count, time until it can run again]
        queue, time = deque(), 0

        # Getting the minimum amount of idle time necessary
        while max_heap or queue:
            time += 1

            if max_heap:
                count = 1 + heappop(max_heap)
                # Adding the count and time it'll be available to our queue
                if count:
                    queue.append([count, time + n])

            # We can run this task again
            if queue and queue[0][1] == time:
                heappush(max_heap, queue.popleft()[0])

        return time

# Time Complexity: O(n), worst case it'd be O(n)*log(26) but that simplifies to O(n)
# Space Complexity: O(n)