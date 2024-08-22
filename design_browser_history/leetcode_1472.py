import typing


class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None
        self.prev = None


class BrowserHistory:
    def __init__(self, homepage: str):
        self.head = Node(homepage)

    def visit(self, url: str) -> None:
        new_page = Node(url)  # create the new page node
        new_page.prev = self.head  # connect previous page to the current page [prev_page <- current_page]
        self.head.next = new_page  # connect previous page's next page to the current page [prev_page -> current_page]
        self.head = self.head.next  # move the pointer to the current page
    
    def back(self, steps: int) -> str:
        while steps and self.head.prev:
            self.head = self.head.prev
            steps -= 1
        return self.head.data
    
    def forward(self, steps: int) -> str:
        while steps and self.head.next:
            self.head = self.head.next
            stesp -= 1
        return self.head.data
    

