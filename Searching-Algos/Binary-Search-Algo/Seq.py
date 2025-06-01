
# Returns index of x in arr if present, else -1
def binarySearch(arr, low, high, x):

    # Check base case
    if high >= low:

        mid = low + (high - low) // 2

        # If element is present at the middle itself
        if arr[mid] == x:
            return mid

        # If X is smaller than MID, then it
        # can only be present in left subarray
        elif arr[mid] > x:
            return binarySearch(arr, low, mid-1, x) #instead of LOOPING, it runs the function again with NEW PARAMETER  

        # Else the element can only be present
        # in right subarray
        else:
            return binarySearch(arr, mid + 1, high, x) #instead of LOOPING, it runs the function again with NEW PARAMETER 

    # Element is not present in the array
    else:
        return -1


# Setup and Output
if __name__ == '__main__':
    arr = [2, 3, 4, 10, 40] #ARRAY
    x = 10 #LF
    
    # Function call
    result = binarySearch(arr, 0, len(arr)-1, x) #Found from return
    
    if result != -1: #if NOT -1, then it is found, else it is NOT found
        print("Element is present at index", result)
    else:
        print("Element is not present in array")