#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
this is a file to test different sorting algorithms
"""
import random
import datetime


def get_time():
    """
    returns time stamp in milliseconds
    """
    return int(datetime.datetime.now().strftime("%S%f"))


class MyList(list):

    """
    an extention of the list class
    """
    N = 100

    def bubble(self, i):
        """
        move the elem at index i though the array using the bubble algorithm
        """
        if self[i - 1] > self[i]:
            j = i - 1
            while self[j] > self[i]:
                j -= 1
                continue
            if j < 0:
                self.insert(0, self.pop(i))
            else:
                self.insert(j + 1, self.pop(i))
            return True  # moved the item !
        return False  # didn't move the item!

    @classmethod
    def sortAndPrint(cls, name=None, n=None, *args, **kwargs):
        """
        helper method to print time data on sorting
        """
        if not n:
            n = cls.N
        data = cls(range(0, n))
        random.shuffle(data)
        start_time = get_time()
        data.sort(name)
        print 'Sorted %d elements in %s milliseconds\n' % \
            (len(data), ((get_time() - start_time) / 1000.0))

    def sort(self, name=None, *args, **kwargs):
        """
        overide sort method
        """
        if not name:
            print 'Sorting %s with default algorithm' % self[:10]
            return super(MyList, self).sort(*args, **kwargs)
        print 'Sort %s with %s algorithm' % (self[:10], name)
        if name == 'bubble':
            i = len(self)
            cursor = i - 1
            while cursor > 0:
                    # return
                res = self.bubble(cursor)
                if res:
                    cursor = i - 1
                else:
                    cursor -= 1
        if name == 'insert':
            for i in range(1, len(self)):
                j = i - 1
                while j >= 0 and self[i] < self[j]:
                    j -= 1
                if j + 1 != i:
                    if j < 0:
                        self.insert(0, self.pop(i))
                    else:
                        self.insert(j + 1, self.pop(i))
        if name == 'select':
            for i in range(0, len(self)):
                smallest = i
                for j in range(i + 1, len(self)):
                    if self[j] < self[smallest]:
                        smallest = j
                self.insert(i, self.pop(smallest))
        return self

N = 100

MyList.sortAndPrint('bubble', N)
MyList.sortAndPrint('insert', N)
MyList.sortAndPrint('select', N)
