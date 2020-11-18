
def binary_search_first(arr, x): 
    low = 0
    high = len(arr) - 1
    mid = 0
    index = -1
  
    while low <= high: 
  
        mid = low + (high - low) // 2
  
        # Check if x is present at mid
        

        if arr[mid] < x: 
            # Change the window so that the upper boundary is mid point 
            low = mid  + 1

        else:
            # change the window so that it is smaller on the right side
            high = mid - 1 

        if arr[mid] == x:
            index = mid   

   
 
    return index

def binary_search_last(arr, x): 
    low = 0
    high = len(arr) - 1
    mid = 0
    index = -1
  
    while low <= high: 
  
        mid = low + (high - low) // 2
  
        # Check if x is present at mid
    
        if arr[mid] > x: 
            # Change the window so that the upper boundary is mid point 
            high = mid  - 1

        else:
            # change the window so that it is smaller on the right side
            low = mid + 1 

        if arr[mid] == x:
            index = mid   

   
 
    return index

def return_sum_of_integers(arr,l,r):

    print(l,r)
    return len(arr[l:r])
  

array = [1,2,2,2,2,2,2,2,3,3,3,3,4,5,6,7,78]

l = binary_search_first(array, 2)
r = binary_search_last(array, 2)
print(return_sum_of_integers(array,l,r))
