#!/usr/bin/env python
"""
BinManager


The main program logic for the package. BinPack manages
creation and ranking of bins and returns layout dictionaries
for packed bins.

"""
from typing import List
from item import Item
import shelf


class BinManager:
    """
    Interface Class.
    """
    def __init__(self, bin_width: int = 8, bin_height: int = 4) -> None:
        self.bin_width = bin_width
        self.bin_height = bin_height
        self.items = []
        self.bins = []
        self.bin_count = 0
        self.algorithm = 'shelf'
        self.heuristic = 'next_fit'


    def add_items(self, *items: List[Item]) -> bool:
        for item in items:
            self.items.append(item)
        self.items.sort(key=lambda el: el.x*el.y, reverse=True)


    def set_algorthim(self, family: str, heuristic: str) -> bool:
        if family == 'shelf':
            self.algorithm = shelf.Sheet(self.bin_width, self.bin_height)
            if heuristic == 'next_fit':
                self.heuristic = 'next_fit'
                return True
            elif heuristic == 'first_fit':
                self.heuristic = 'first_fit'
                return True
            elif heuristic == 'best_width_fit':
                self.heuristic = 'best_width_fit'
                return True
            elif heuristic == 'best_height_fit':
                self.heuristic = 'best_height_fit'
                return True
            elif heuristic == 'best_area_fit':
                self.heuristic = 'best_area_fit'
                return True
            elif heuristic == 'worst_area_fit':
                self.heuristic = 'worst_area_fit'
                return True

        elif family == 'guillotine':
            return
        else:
            return 'sorry we dont support that algorithm'

    def execute(self) -> None:
        for item in self.items:
            self.algorithm.insert(item, self.heuristic)

        print(self.algorithm)
        for i, shelf in enumerate(self.algorithm.shelves):
            print('Shelf #%s: %r' % (i, str(shelf.items)))


if __name__ == '__main__':
    MANAGER = BinManager()
    MANAGER.add_items(Item(2,6), Item(3,2), Item(1,1))
    MANAGER.set_algorthim('shelf', 'worst_width_fit')
    MANAGER.execute()