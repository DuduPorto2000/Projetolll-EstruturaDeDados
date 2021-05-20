##############################################
################## Imports ###################
##############################################

import random
import time
import sys
import copy

sys.setrecursionlimit(50000)

##############################################
################## Chaves ####################
##############################################

keys = []
for i in range(20000):
    keys.append(random.randint(1, 5000))

##############################################
################ BubbleSort ##################
##############################################

def bubble_sort(array):
    elementos = len(array)-1
    order = False
    while not order:
        order = True
        for i in range(elementos):
            if array[i] > array[i+1]:
                array[i], array[i+1] = array[i+1], array[i]
                order = False
    return array
  
ini = time.time()
bubble_array = bubble_sort(copy.deepcopy(keys))
fim = time.time()
bubble_time = fim-ini

##############################################
################ InsertSort ##################
##############################################

def insertion_sort(array): 
    for i in range(1, len(array)):
        key = array[i]
        j = i-1
        while j >= 0 and key < array[j]:
            array[j+1] = array[j]
            j -= 1
        array[j+1] = key

copyInsert = copy.deepcopy(keys)
ini = time.time()
insertion_sort(copyInsert)
fim = time.time()
insert_time = fim-ini

##############################################
################# ShellSort ##################
##############################################

def shell_sort(array):
    n = len(array)
    interval = n // 2
    while interval > 0:
        for i in range(interval, n):
            temp = array[i]
            j = i
            while j >= interval and array[j - interval] > temp:
                array[j] = array[j - interval]
                j -= interval
            array[j] = temp
        interval //= 2

copyShell = copy.deepcopy(keys)
ini = time.time()
shell_sort(copyShell)
fim = time.time()
shell_time = fim-ini

##############################################
################# QuickSort ##################
##############################################

def partition(array, begin, end):
    pivot = begin
    for i in range(begin+1, end+1):
        if array[i] <= array[begin]:
            pivot += 1
            array[i], array[pivot] = array[pivot], array[i]
    array[pivot], array[begin] = array[begin], array[pivot]
    return pivot

def quick_sort(array, begin=0, end=None):
    if end is None:
        end = len(array) - 1
    def _quick_sort(array, begin, end):
        if begin >= end:
            return
        pivot = partition(array, begin, end)
        _quick_sort(array, begin, pivot-1)
        _quick_sort(array, pivot+1, end)
    return _quick_sort(array, begin, end)

copyQuick = copy.deepcopy(keys)
ini = time.time()
quick_sort(copyQuick)
fim = time.time()
quick_time = fim-ini

##############################################
################# MergeSort ##################
##############################################

def merge_sort(alist):
    if len(alist)>1:
        mid = len(alist)//2
        lefthalf = alist[:mid]
        righthalf = alist[mid:]
        merge_sort(lefthalf)
        merge_sort(righthalf)

        i=0
        j=0
        k=0

        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                alist[k]=lefthalf[i]
                i=i+1
            else:
                alist[k]=righthalf[j]
                j=j+1
            k=k+1

        while i < len(lefthalf):
            alist[k]=lefthalf[i]
            i=i+1
            k=k+1

        while j < len(righthalf):
            alist[k]=righthalf[j]
            j=j+1
            k=k+1

copySort = copy.deepcopy(keys)
ini = time.time()
merge_sort(copySort)
fim = time.time()
merge_time = fim-ini

##############################################
################## Prints ####################
##############################################

print('')
print('BubbleSort')
print(f'{len(bubble_array)} Chaves Ordenadas')
print(f'Tempo Gasto: {bubble_time}s')
print('')


print('InsertSort')
print(f'{len(copyInsert)} Chaves Ordenadas')
print(f'Tempo Gasto: {insert_time}s')
print('')


print('ShellSort')
print(f'{len(copyShell)} Chaves Ordenadas')
print(f'Tempo Gasto: {shell_time}s')
print('')


print('QuickSort')
print(f'{len(copyQuick)} Chaves Ordenadas')
print(f'Tempo Gasto: {quick_time}s')
print('')


print('MergeSort')
print(f'{len(copySort)} Chaves Ordenadas')
print(f'Tempo Gasto: {merge_time}s')
print('')