def binary_search(arr, target):
    """Perform binary search on a sorted array.

    Args:
        arr (list): A sorted list of elements to search.
        target: The element to search for.

    Returns:
        int: The index of the target element if found, otherwise -1.
    """
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = left + (right - left) // 2

        # Check if target is present at mid
        if arr[mid] == target:
            return mid
        # If target is greater, ignore left half
        elif arr[mid] < target:
            left = mid + 1
        # If target is smaller, ignore right half
        else:
            right = mid - 1

    # Target was not found in the array
    return -1

# Example usage:
sorted_arr = [1, 2, 3, 4, 5]
target = 3
result = binary_search(sorted_arr, target)
print(f"Element {target} found at index: {result}")  # Output: Element 3 found at index: 2