import random

import time


def bubble_sort():
    for i in range(len(x)):
        for j in range((i + 1), len(x)):
            if x[i] > x[j]:
                x[i], x[j] = x[j], x[i]



def selection():
    for i in range(len(x)):
    least = i 
    for j in range((i+1), len(x)): 
        if x[least] > x[j]: 
            least = j       
    x[i], x[least] = x[least], x[i] 


def insertion():
    for i in range(1, len(x)):
        key = x[i]
        j = i - 1
        while j >= 0 and key < x[j]:
            x[j + 1] = x[j]
            j -= 1
        x[j + 1] = key


def linear():
    key = False

    for i in range(len(x)):

        if x[i] == find:
            key = True

            print('found', find, 'at', i)

            break

    if (key == False):
        print('not found')


def binary():
    t1 = time.time()
    bubble_sort()
    t2 = time.time()
    print('bubble_sort time', t2 - t1)

    t1 = time.time()
    selection()
    t2 = time.time()
    print('selection_sort time', t2 - t1)

    t3 = time.time()
    insertion()
    t4 = time.time()
    print('insertion_sort time', t4 - t3)

    x1 = x

    first = 0

    last = len(x1) - 1

    mid = int((first + last) / 2)

    while (first <= last):

        if (find > x1[mid]):

            first = mid + 1

        elif (find == x1[mid]):

            print('found', find, 'at', mid)

            break

        else:

            last = mid - 1

        mid = int((first + last) / 2)

    if (first > last):
        print('not found')


x = random.sample(range(0, 100), 10)

print(x)

find = int(input('enter the search element'))

start_time = time.time()

linear()

end_time = time.time()

print('linear time', end_time - start_time)

start = time.time()

binary()

end = time.time()

print('binary time', end - start)
