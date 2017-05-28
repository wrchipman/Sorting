#!/usr/bin/env python

from quicksort import QuickSort
from bubblesort import BubbleSort
from selectionsort import SelectionSort
import datetime
import random
import copy


test_list = []
for i in range(10000):
    test_list.append(random.randint(0, 100000000))

qs_list = copy.deepcopy(test_list)
bs_list = copy.deepcopy(test_list)
ss_list = copy.deepcopy(test_list)


start_time = datetime.datetime.now()
QuickSort(qs_list)
total_time = datetime.datetime.now() - start_time
print "QuickSort took " +  str(total_time)


start_time = datetime.datetime.now()
BubbleSort(bs_list)
total_time = datetime.datetime.now() - start_time
print "BubbleSort took " +  str(total_time)

start_time = datetime.datetime.now()
SelectionSort(ss_list)
total_time = datetime.datetime.now() - start_time
print "SelectionSort took " +  str(total_time)
