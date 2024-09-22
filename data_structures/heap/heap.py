def heapify(array,n,i):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2


    if l < n and array[l] > array[largest]:
        largest = l
    if r < n and array[r] > array[largest]:
        largest = r    

    if largest!=i:
        array[i],array[largest] = array[largest],array[i]
        heapify(array,len(array),largest)

def insert(array,NewNum):
    array.append(NewNum)
    current = len(array) - 1
    while current>0:
        parent = (current - 1) //2
        if array[current] > array[parent]:
            array[current],array[parent] = array[parent],array[current]
        else:
            break    

def delete_Node(array,num):
    size = len(array)
    i = 0
    for i in range(size):
        if array[i] == num:
            break 
    array[i],array[-1] = array[-1],array[i]
    array.pop()

    if i<len(array):
        heapify(array,len(array),i)           


#MaxHeap(array, size)
 # loop from the first index of non-leaf node down to zero
 #   call heapify       