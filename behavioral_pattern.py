# Iterator behavioral pattern
from __future__ import annotations
from collections.abc import Iterable, Iterator
from typing import Any


class LenSetIterator(Iterator):
    _pos: int = None
    _desc: bool = False

    def __init__(self, set_collection, desc: bool = False) -> None:
        self._collection = set_collection
        self._desc = desc
        self._position = -1 if desc else 0

    def __next__(self):
        try:
            value = self._collection[self._position]
            self._position += -1 if self._desc else 1
        except IndexError:
            raise StopIteration()

        return value


class SetCollection(Iterable):
    def __init__(self, collection=None) -> None:
        if collection is None:
            collection = []
        self._collection = sorted(collection, key=len)

    def __iter__(self) -> LenSetIterator:
        return LenSetIterator(self._collection)

    def get_reverse_iterator(self) -> LenSetIterator:
        return LenSetIterator(self._collection, True)

    def add_item(self, item: Any):
        self._collection.append(item)
        self._collection = sorted(self._collection, key=len)


def main():
    collection = SetCollection([{1, 2, 3}, {1, 2, 4, 3}, {123}])
    collection.add_item({1,23})
    print(collection._collection)
    for set_var in collection:
        print(set_var)


if __name__ == '__main__':
    main()
