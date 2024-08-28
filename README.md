# T2A1-B: Workbook Part B 

PGM1004-6.1: Demonstrates algorithmic understanding
4 to >3.33 pts
HD
Provides a full and clear explanation for all algorithms, showcasing exceptional understanding in each explanation.

Provides clear explanations for all four algorithms, describing how the Big O notation numbers were calculated. Demonstrates an excellent understanding of the relationship between algorithmic structures and Big O complexity.

Provides a comprehensive evaluation of algorithm efficiency using Big O notation. Explicitly compares the two algorithms in each pair and considers their practical applicability. Provides insightful discussions on edge cases. Demonstrates a high-level understanding of the implications of time complexity in practical use cases.

## Big 0 Notation

Big O notation is used to describe the time complexity and efficiency of algorithms. This notation puts the number of steps in the spotlight and the hardware is not taken into consideration. Big O notation always takes the worse case scenario.

## Types of complexity:

### O(1) Constant

As the data grows, the number of steps stays the same, no matter how small or big the data is. In this algorithm a value will be selected and return. In the example bellow, no matter how many items are in this array, the function with return the element with the index value of 0.

#### Example of Constant time complexity algorithm

    def get_first_element(arr):
    return arr[0]

### O(log n) Logarithmic

As the data grows large, the Logarithmic complexity becomes smaller relative to the growth. More data = less steps. This type of algorithm is usually found in algorithms that usually `halve` data such as Binary search.

- Data size grows large and complexity becomes smaller
- Always involve some type of division, example of binary search
- Each time through the loop, the data set to search is halved
- Algorithm will require (log n) steps 
- The max number of steps is the power of 2. 

#### Pseudo-code
    # Mid point = L / 2
    # Mid-point value = arr[midpoint] 
    # IF value == mid-point:
        # return value or index

    # IF value < mid-point:
        # discard the upper-part of the array
    # ELSE if value > element:
    # discard the lower part of the array

#### Function to find the X value, and how many steps it takes
    def binary_search_with_steps(arr, x):
        # Set low side of array to 0
        low = 0
        # Set high to the array length -1 to access index
        high = len(arr) - 1
        # Initialise steps to zero
        steps = 0
        
        # While loop, half the array to find the MID array
        # Increment the steps to 1
        while low <= high:
            steps += 1  
            mid = (low + high) // 2
            
            if arr[mid] == x:
                return mid, steps  
            elif arr[mid] < x:
                low = mid + 1
            else:
                high = mid - 1
        
        return -1, steps  

    print(binary_search_with_steps([1, 5, 8, 12, 20, 21, 35], 8))


### O(n) Linear

As the size of the dataset increases, the time complexity grows at the same rate. In the worst case, the algorithm requires a number of steps equal to the number of elements in the input dataset.

#### Function that counts the occurrences of a value in an input dataset

    def count_values(arr, val):
        count = 0
        for each in arr:
            if each == val:
                count += 1 
        
        return f"Occurrence of {val} value is {count} times."

    print(count_values([1,2,1,1,3],1))

### O(n^2) Quadratic

Typically involves nested loops, where the time complexity increases quadratically as the size of the input data grows.

#### Example Bubble algorithm that compares each value to each other value 

    def bubble_sort(arr):
        n = len(arr)
        for i in range(n):
            for j in range(0, n-i-1):
                if arr[j] > arr[j+1]:
                    arr[j], arr[j+1] = arr[j+1], arr[j]
        return arr

    print(bubble_sort([64, 34, 25, 12, 22, 11, 90]))


### O(2n) Exponential

This algorithm grows the quickest, algorithm steps doubles with addition to dataset. This is common in recursing algorithms that call themselves multiple times. Exponential algorithms should be avoided because it has very high complexity and uses a lot of memory.

#### Fibonacci example 

    def fibonacci(n):
        if n <= 0:
            return 0
        elif n == 1:
            return 1
        else:
            # Function calls itself twice here
            return fibonacci(n-1) + fibonacci(n-2) 

    # Example usage
    print(fibonacci(3))


## Types of algorithms:

- Searching Algorithm

- Sorting Algorithms

- Counting Algorithms

- Graph Algorithms


# Q1 

### Bubble Sort - O(n^2)

Bumble sort is a type of Sorting Algorithm. Sorting algorithm is the number of steps it takes to put a list in a specific order, example: smallest to largest, ascending or descending. The main goal of this algorithm is to organise data so data can be easily read and searched through. Sorting algorithm includes Quick Sort, Merge Sort, Bubble Sort, and Selection Sort.

A Bubble Sorting Algorithm compares each element with each other element, swapping them if needed to achieve an organised order. This process involves comparing adjacent elements and swapping them to ensure the larger elements "bubble up" to their correct positions, hence the name "Bubble Sort."

Bubble Sort uses nested loops: an outer loop and an inner loop. Both loops have linear complexity, and when combined, this results in a quadratic complexity, represented as O(n²).

Outer Loop: The outer loop runs through the list or array multiple times until the entire list is sorted. If the array has `n` elements, this loop typically runs `n-1` times.
Inner Loop: The inner loop compares adjacent elements within the list. If the current element is greater than the next element, they get swapped, if the current element is smaller, nothing gets done and the loop continues. As the sorting progresses, larger elements gradually move towards their correct positions, and the number of iterations needed decreases.

Bubble Sort algorithm is represented by O(n^2) Quadratic complexity in Big O notation. Big O notations always consider the worst case scenario. However, complexity notations can change depending if algorithm complexity increases or decreases. Bubble sort best case scenario occurs when array is sorted already and swapped flag is used, this will improve complexity from O(n^2) to O(n) - Linear complexity due to the outer loop running only once.

Considering the `Best case scenario` in Bubble Sort with the arr = [1, 2, 3, 4, 6, 33] and swap flag (Boolean value), the algorithm will improve to Linear complexity since the list is already ordered. The outer loop will run once, the inner loop will run `n - 1` times and the loop will exit after no swaps were performed. The total number of steps taken in this scenario is 5. 

Quadratic complexity is usually found in algorithms that perform nested loops to compare elements, other algorithms that also has this type of complexity are Selection Sort and Insertion Sort.

Quadratic has a very high complexity, and the reason for that is because the number of steps increases proportionally to the square of the input size. These algorithms performs operations and comparisons on each element against each other element in the list.

Some positive points about the Bubble Algorithm include being simple to understand and easy to implement. Due to it's simplicity it's great for educational purposes. It can be more suited to small and simple tasks rather then more complex algorithms. It's a stable algorithm which means it preserves the order of elements with equal values, this is crucial when sorting algorithm by multiple criteria. However, this algorithm becomes very inefficient when dealing with larger datasets due to the fact as the input increases, the complexity grows extremely fast.  


### Worse case scenario
In this scenario, the order is in inverse, which means the loops will interact over all elements and perform the maximum number of operations (swaps) to sort elements. 

    def bubbleSort(arr):
        # 'n' variable stores the elements of the list
        n = len(arr)
        
        # Outer loop runs 'n' times
        # Each run ensures larger numbers are placed towards the end of the list 
        for i in range(n):

            # Inner loop runs from the first to last element minus the ordered elements
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
    No comparisons are needed since only one element is left unsorted (smallest element).
    List is sorted.
    Final Sorted List:
    [1, 2, 3, 4, 6, 33]


### Average case scenario
Using the `swap` Boolean flag, the loops are able to terminate earlier if list is already sorted thereby eliminating the need to complete all interactions, this increases efficiency. The example bellow presents the same code with Boolean flag added. This still a quadratic complexity.

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



# Q2	
Identify and explain the workings of TWO search algorithms and discuss and compare their performance/efficiency (i.e. Big O)	Minimum 300

### Quick Sort











References:

Notes taken by myself from ED/Canvas and past Zoom classes.

GeeksforGeeks. (2014). Bubble Sort Algorithm. [online] Available at: https://www.geeksforgeeks.org/bubble-sort-algorithm/.

geeksforgeeks (2018). Analysis of Algorithms | Big-O analysis - GeeksforGeeks. [online] GeeksforGeeks. Available at: https://www.geeksforgeeks.org/analysis-algorithms-big-o-analysis/.
