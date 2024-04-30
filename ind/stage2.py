from typing import Any, List

class Iterator:
    def __init__(self, collection: List[Any]):
        self._collection = collection
        self._index = 0

    def first(self) -> None:
        self._index = 0

    def next(self) -> None:
        self._index += 1

    def is_done(self) -> bool:
        return self._index >= len(self._collection)

    def current_item(self) -> Any:
        return self._collection[self._index]

class Aggregate:
    def __init__(self):
        self._items = []

    def add_item(self, item: Any) -> None:
        self._items.append(item)

    def create_iterator(self) -> Iterator:
        return Iterator(self._items)

    def create_reverse_iterator(self) -> Iterator:
        return Iterator(self._items[::-1])

def client_code(collection: Aggregate) -> None:
    print("\nПерший елемент:")
    iterator = collection.create_iterator()
    iterator.first()
    print(iterator.current_item())

    print("\nВесь список:")
    iterator.first()
    while not iterator.is_done():
        item = iterator.current_item()
        print(item)
        iterator.next()

    print("\nСписок у зворотньому порядку:")
    reverse_iterator = collection.create_reverse_iterator()
    reverse_iterator.first()
    while not reverse_iterator.is_done():
        item = reverse_iterator.current_item()
        print(item)
        reverse_iterator.next()

if __name__ == "__main__":
    collection = Aggregate()
    collection.add_item("Item 1")
    collection.add_item("Item 2")
    collection.add_item("Item 3")

    client_code(collection)