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

        visited, path, i = set(), defaultdict(list), 0
        def dfs(node, i):
            path[i].append(node)
            visited.add(node)

            for nei in adj[node]:
                if nei not in visited:
                    dfs(nei, i)

        # DFS
        for email in adj:
            if email in visited:
                continue

            dfs(email, i)
            i += 1

        # Getting it in the proper format
        res = []
        for emails in path.values():
            res.append([emailToName[emails[-1]]] + sorted(emails))

        return res

# TC: O(nlogn)
# SC: O(V) + O(E)
# Solution: https://leetcode.com/problems/accounts-merge/discuss/1602173/Python-simple-dfs-explained