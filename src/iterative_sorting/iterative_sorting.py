# TO-DO: Complete the selection_sort() function below 
def selection_sort( arr ):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc) 
        
        # second index compared to first
        # if second is larger, compare third to second.
        # if it is less than the one it is being compared to, keep it in front.
        # if it is more, compare it to the next index.   repeat 
def selection_sort( arr ):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # find next smallest element
        for j in range(cur_index, len(arr)):
            if arr[j] < arr[smallest_index]:
                smallest_index = j

        # swap
        temp = arr[smallest_index]
        arr[smallest_index] = arr[cur_index]
        arr[cur_index] = temp

    return arr

        
        
        
        
        # while cur_index > 0 and arr[i] < arr[cur_index - 1]:
        #     arr[i], arr[j - 1] = arr[j - 1], arr[i]
        #     cur_index -= 1



        # TO-DO: swap
        # if the initial index is more than the one it is being compared to, 



    return arr




selection_sort([6, 8, 12, 4, 2, 9, 7, 3, 1])


# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):

    return arr


# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr


    