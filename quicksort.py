#!/usr/bin/env python

class QuickSort(object):
    def __init__(self, sorting_list = []):
        #print sorting_list
        self.quick_sort_main(sorting_list, 0, len(sorting_list)-1)
        #print sorting_list
        #return sorting_list

    def quick_sort_main(self, sorting_list, first, last):
        if first <last:
            split_point = self.sub_division(sorting_list, first, last)

            self.quick_sort_main(sorting_list, first, split_point-1)
            self.quick_sort_main(sorting_list, split_point+1, last)

    def sub_division(self, sorting_list, first, last):
        pivot_value = sorting_list[first]

        left_pointer = first + 1
        right_pointer = last

        done = False
        while not done:

            while left_pointer <= right_pointer and \
                  sorting_list[left_pointer] <= pivot_value:
                left_pointer = left_pointer + 1

            while sorting_list[right_pointer] >= pivot_value and \
                  right_pointer >= left_pointer:
                right_pointer = right_pointer - 1

            if right_pointer < left_pointer:
                done = True

            else:
                temp = sorting_list[left_pointer]
                sorting_list[left_pointer] = sorting_list[right_pointer]
                sorting_list[right_pointer] = temp

        temp = sorting_list[first]
        sorting_list[first] = sorting_list[right_pointer]
        sorting_list[right_pointer] = temp

        return right_pointer
