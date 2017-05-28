#!/usr/bin/env python

class SelectionSort(object):
    def __init__(self, sorting_list):
        self.selection_sort_func(sorting_list)

    def selection_sort_func(self, sorting_list):
        for passnum in range(len(sorting_list)-1, 0, -1):
            max_num_pos = 0
            for location in range(1, passnum+1):
                if sorting_list[location]>sorting_list[max_num_pos]:
                    max_num_pos = location

            sorting_list[passnum], sorting_list[location] = \
            sorting_list[location], sorting_list[passnum]
