#!/usr/bin/env python

class BubbleSort(object):
    def __init__(self, sorting_list):
        self.bubble_sort_func(sorting_list)


    def bubble_sort_func(self, sorting_list):
        for passnum in range(len(sorting_list)-1, 0, -1):
            for num in range(passnum):
                if sorting_list[num] > sorting_list[num+1]:
                    sorting_list[num], sorting_list[num+1] = \
                    sorting_list[num+1], sorting_list[num]
