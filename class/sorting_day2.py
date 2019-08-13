class Book:
    def __init__(self, title, name, genre):
        self.title = title
        self.name = name
        self.genre = genre



# recursion
def foo(n):
    foo(n-1)

# fibonnacci sequence
0 1 2 3 4 5 6 7 8
0 1 1 2 3 5 8 13 21 

fib(n) == fib(n-1) + fib(n-2)

def fib(n):
    if n == 0: 
        return 0

    if n == 1:
        return 1

    return fib(n-1) + fib(n-2)



# quicksort
# partitioning step

5 3 8 2 9 4 1 7

1.  choose the pivot

!
5 3 8 2 9 4 1 7 

2. partition

3 2 4 1 # less than pivot 
5       # pivot
8 9 7   # greater than

3. combine
3 2 4 1    5    8 9 7


def partition(l):
    left = []
    pivot = l[0]
    right = []

    for v in l[1:]:
        if v <= pivot:
            left.append(v)
        else:
            right.append(v)
    
    return left, right, pivot

def quicksort(l):
    if len(l) <= 1:
        return l

    left, pivot, right = partition(l)
    return quicksort(left) + [pivot] + quicksort(right)