# T2A1-B: Workbook Part B 

PGM1004-6.1: Demonstrates algorithmic understanding
4 to >3.33 pts
HD
Provides a full and clear explanation for all algorithms, showcasing exceptional understanding in each explanation.

Provides clear explanations for all four algorithms, describing how the Big O notation numbers were calculated. Demonstrates an excellent understanding of the relationship between algorithmic structures and Big O complexity.

Provides a comprehensive evaluation of algorithm efficiency using Big O notation. Explicitly compares the two algorithms in each pair and considers their practical applicability. Provides insightful discussions on edge cases. Demonstrates a high-level understanding of the implications of time complexity in practical use cases.


# Types of algorithms

- Sorting algorithm 
Sorting algorithm is the number of steps it takes to put a list in a specific order, example: smallest to largest, ascending or descending. The main goal of this algorithm is to organise data so data can be easily read and searched through. Sorting algorithm includes Quick Sort, Merge Sort, Bubble Sort, and Selection Sort. 

- Searching Algorithm

- Counting Algorithm


# Q1 

### Bubble Sort - O(n^2)

A bubble sorting algorithm compares each value to each other value. It works by comparing adjacent numbers (numbers next to each other) and swapping them if needed to create an organised array or list. Bubble sort contains nested loops, the outer loop and the inner loop are both linear complexity and when you add those two loops together, it results in quadratic complexity. 

The outer loop runs through the list or array multiple times until sorting has been completed, if the array has `n` elements, the loop typically runs `n-1` times. 
The inner loop compares adjacent numbers and swap them if needed. As the numbers get sorted, the numbers get "bubble up" in the correct order and the number of interactions gets smaller.

Big O notation always considers the worst-case scenario. For the Bubble Sort algorithm, this means that the loop will execute n times. Therefore, Bubble Sort is represented by O(n^2) quadratic complexity in Big O notation. It's better to avoid this algorithm when dealing with larger databases and reverse-sorted lists however it can be beneficial for small databases and for learning purposes. 

Some positive points about the Bubble sort includes being simple to understand and easy to implement, it's a stable algorithm which means it preserves the order of elements with equal values, it's crucial point when sorting algorithm by multiple criteria. Some negative points makes this type of algorithm inefficient including slow process in larger data, since algorithm compares each element to each other element in the array and it also requires a comparison operator which also adds to processing time. 

### Worse case scenario
In this scenario, the order is in inverse, which means the loops will interact over all elements in the list and perform the maximum number of operations (swaps) to sort elements. 

    def bubbleSort(arr):
        # 'n' variable stores the elements of the list
        n = len(arr)
        
        # Outer loop runs 'n' times
        # Each run ensures larger numbers are placed towards the end of the list 
        for i in range(n):

            # Inner loop runs from the first element to the last element minus the ordered elements
            for j in range(0, n-i-1):
                # Compares the actual element with the next element (adjacent pairs)
                # If the actual element is greater than actual, it swap places
                # Larger element moves to the right hand side
                if arr[j] > arr[j+1]:
                    arr[j], arr[j+1] = arr[j+1], arr[j]
                
    # Example list
    arr = [33, 6, 4, 3, 2, 1]

    # Sort the list
    bubbleSort(arr)

    # Print the sorted list
    print("Sorted list:", arr)

### Step-by-Step Sorting Process:

Pass 1:
arr = [33, 6, 4, 3, 2, 1]
Compare 33 and 6: Since 33 > 6, swap them.
List after swap: [6, 33, 4, 3, 2, 1]
Compare 33 and 4: Since 33 > 4, swap them.
List after swap: [6, 4, 33, 3, 2, 1]
Compare 33 and 3: Since 33 > 3, swap them.
List after swap: [6, 4, 3, 33, 2, 1]
Compare 33 and 2: Since 33 > 2, swap them.
List after swap: [6, 4, 3, 2, 33, 1]
Compare 33 and 1: Since 33 > 1, swap them.
List after swap: [6, 4, 3, 2, 1, 33]
Result after Pass 1: [6, 4, 3, 2, 1, 33]
The largest element, 33, has "bubbled" to its correct position at the end.

Pass 2:
Compare 6 and 4: Since 6 > 4, swap them.
List after swap: [4, 6, 3, 2, 1, 33]
Compare 6 and 3: Since 6 > 3, swap them.
List after swap: [4, 3, 6, 2, 1, 33]
Compare 6 and 2: Since 6 > 2, swap them.
List after swap: [4, 3, 2, 6, 1, 33]
Compare 6 and 1: Since 6 > 1, swap them.
List after swap: [4, 3, 2, 1, 6, 33]
Result after Pass 2: [4, 3, 2, 1, 6, 33]
The second largest element, 6, is now in its correct position, just before 33.

Pass 3:
Compare 4 and 3: Since 4 > 3, swap them.
List after swap: [3, 4, 2, 1, 6, 33]
Compare 4 and 2: Since 4 > 2, swap them.
List after swap: [3, 2, 4, 1, 6, 33]
Compare 4 and 1: Since 4 > 1, swap them.
List after swap: [3, 2, 1, 4, 6, 33]
Result after Pass 3: [3, 2, 1, 4, 6, 33]
The third largest element, 4, is now in its correct position.

Pass 4:
Compare 3 and 2: Since 3 > 2, swap them.
List after swap: [2, 3, 1, 4, 6, 33]
Compare 3 and 1: Since 3 > 1, swap them.
List after swap: [2, 1, 3, 4, 6, 33]
Result after Pass 4: [2, 1, 3, 4, 6, 33]
The fourth largest element, 3, is now in its correct position.

Pass 5:
Compare 2 and 1: Since 2 > 1, swap them.
List after swap: [1, 2, 3, 4, 6, 33]
Result after Pass 5: [1, 2, 3, 4, 6, 33]
The fifth largest element, 2, is now in its correct position.

Pass 6:
No comparisons are needed since only one element is left unsorted, and the list is now fully sorted.
Final Sorted List:
[1, 2, 3, 4, 6, 33]


### Average case scenario
Using the `swap` Boolean flag, the loops are able to terminate earlier if list is already sorted thereby eliminating the need to complete all interactions, this increases efficiency. The example bellow presents the same code with Boolean flag added.

    def bubbleSort(arr):
        # 'n' variable stores the elements of the list
        n = len(arr)
        
        # Outer loop runs 'n' times
        # Each run ensures larger numbers are placed towards the end of the list
        # Swap checks if elements have been swapped 
        for i in range(n):
            swapped = False

            # Inner loop runs from the first element to the last element minus the ordered elements
            for j in range(0, n-i-1):
                # Compares the actual element with the next element (adjacent pairs)
                # If the actual element is greater than actual, it swap places
                # Larger element moves to the right hand side
                if arr[j] > arr[j+1]:
                    arr[j], arr[j+1] = arr[j+1], arr[j]
                    # If changes occur, swapped condition = True
                    swapped = True
            # Loop exit if no more swaps are performed, it means list is ordered.
            if (swapped == False):
                break

    # Example list
    arr = [1, 4, 2, 6, 33, 3]

    # Sort the list
    bubbleSort(arr)

    # Print the sorted list
    print("Sorted list:", arr)

References:

GeeksforGeeks. (2014). Bubble Sort Algorithm. [online] Available at: https://www.geeksforgeeks.org/bubble-sort-algorithm/.

‌

# Q2	
Identify and explain the workings of TWO search algorithms and discuss and compare their performance/efficiency (i.e. Big O)	Minimum 300

### Quick Sort

