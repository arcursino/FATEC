#!/usr/bin/python
#blog: xiaorui.cc
#author: rfyiamcool@163.com

from itertools import *
class Round_Robin():

    def __init__(self,data):
        self.data = data
        self.data_rr = self.get_item()

    def cycle(self,iterable):
        saved = []
        for element in iterable:
            yield element
            saved.append(element)
        while saved:
            for element in saved:
                yield element

    def get_item(self):
        count = 0
        for item in self.cycle(self.data):
            count += 1
            yield (count, item)

    def get_next(self):
        return self.data_rr.next()
        

if __name__ == "__main__":
    rr_obj = Round_Robin(['a','b','c'])
    for i in range(50):
        print rr_obj.get_next()
    

