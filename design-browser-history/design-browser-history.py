class BrowserHistory:

    def __init__(self, homepage: str):
        self.browser = deque([homepage])
        self.cursor = 0

    def visit(self, url: str) -> None:
        for _ in range(self.cursor):
            if self.browser:
                self.browser.popleft()
            else:
                break
        self.browser.appendleft(url)
        self.cursor = 0
        

    def back(self, steps: int) -> str:
        self.cursor = min(self.cursor + steps, len(self.browser) - 1)
        return self.browser[self.cursor]
        

    def forward(self, steps: int) -> str:
        self.cursor = max(self.cursor - steps, 0)
        return self.browser[self.cursor]


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)