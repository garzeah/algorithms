class ListNode:
    def __init__(self, val, prev = None, nxt = None):
        self.val = val # Contain url
        self.prev = prev
        self.next = nxt

class BrowserHistory:

    def __init__(self, homepage: str):
        self.history = ListNode(homepage)
        self.curr = self.history


    def visit(self, url: str) -> None:
        new = ListNode(url, self.curr) # Creating a new node and point previous to self.curr
        self.curr.next = new # Point our current position to new position
        self.curr = self.curr.next # Moving current to the new current position


    def back(self, steps: int) -> str:
        while self.curr.prev and steps:
            self.curr = self.curr.prev
            steps -= 1

        return self.curr.val


    def forward(self, steps: int) -> str:
        while self.curr.next and steps:
            self.curr = self.curr.next
            steps -= 1

        return self.curr.val


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)

# Time Complexity: O(n)
# Space Complexity: O(n)