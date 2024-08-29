def merge_sort(arr):
    # Array is sorted, it only has one element
    if len(arr) <= 1:
        return arr
    
    # Divide the array into two halves
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]
    
    # Sort arrays and store values in variables 
    left_sorted = merge_sort(left_half)
    right_sorted = merge_sort(right_half)
    
    # Merge the sorted halves
    return merge(left_sorted, right_sorted)


def merge(left, right):
    sorted_arr = []
    i = j = 0
    
    # Compare the elements of the left and right halves and merge them
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            sorted_arr.append(left[i])
            i += 1
        else:
            sorted_arr.append(right[j])
            j += 1
    
    # If there are remaining elements in the left half, add them to the sorted array
    sorted_arr.extend(left[i:])
    
    # If there are remaining elements in the right half, add them to the sorted array
    sorted_arr.extend(right[j:])
    
    return sorted_arr

# Example usage:
arr = [38, 27, 43, 3, 9, 82, 10]
sorted_arr = merge_sort(arr)
print("Sorted array:", sorted_arr)