class ListNode:
    def __init__(self, key, value, next=None) -> None:
        self.key = key
        self.value = value
        self.next = next


class MyHashMap:
    def __init__(self) -> None:
        self.size = 1000
        self.table = [None] * self.size

    def _hash(self, key: int) -> int:
        return key % self.size

    def put(self, key: int, value: int) -> None:
        index = self._hash(key)
        if not self.table[index]:
            self.table[index] = ListNode(key, value)
            return
        current = self.table[index]
        while current:
            if current.key == key:
                current.value = value
                return
            if not current.next:
                current.next = ListNode(key, value)
                return
            current = current.next

    def get(self, key: int) -> int:
        index = self._hash(key)
        current = self.table[index]
        while current:
            if current.key == key:
                return current.value
            current = current.next
        return -1

    def remove(self, key: int) -> None:
        index = self._hash(key)
        current = self.table[index]

        if not current:
            return
        if current.key == key:
            self.table[index] = current.next
            return

        while current.next:
            if current.next.key == key:
                current.next = current.next.next
                return
            current = current.next
