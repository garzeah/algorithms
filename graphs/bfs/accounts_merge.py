class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        adj = defaultdict(set) # Using a set to handle duplicates
        emailToName = {} # Keeping track of which email belongs to which name

        for account in accounts:
            name = account[0]

            for email in account[1:]:
                root = account[1] # Building our node at the first email

                # Building a adj. list out of our emails
                adj[root].add(email)
                adj[email].add(root)
                emailToName[email] = name # Recording owner

        visited, res = set(), []

        # BFS
        for email in adj:
            if email not in visited:
                queue = deque([email])
                visited.add(email)

                local_res = [] # Used to record the emails we visit

                while queue:
                    node = queue.popleft()

                    local_res.append(node)

                    for nei in adj[node]:
                        if nei not in visited:
                            queue.append(nei)
                            visited.add(nei)

                res.append([emailToName[email]] + sorted(local_res))

        return res

# TC: O(nlogn)
# SC: O(V) + O(E)
# Solution: https://www.youtube.com/watch?v=f17PKE8W2p8



