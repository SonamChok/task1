def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

def replace_elements(arr, target, replacement):
    for i in range(len(arr)):
        if arr[i] == target:
            arr[i] = replacement
    return arr

def main():
    # Prompt the user to input an array of integers
    arr = [int(x) for x in input("Enter the array of integers separated by space: ").split()]
    
    # Sort the input array in ascending order using quick sort algorithm
    sorted_arr = quick_sort(arr[:])
    print("Sorted array:", sorted_arr)
    
    # Allow the user to specify a target element to search for in the sorted array
    target = int(input("Enter the target element to search for: "))
    
    # If the target element is found, prompt the user to input a replacement element
    if target in sorted_arr:
        replacement = int(input("Enter the replacement element: "))
        
        # Replace all occurrences of the target element with the replacement element
        modified_arr = replace_elements(sorted_arr[:], target, replacement)
        print("Modified array after replacing the elements:", modified_arr)
    else:
        print("Target element not found in the array.")

if __name__ == "__main__":
    main()
