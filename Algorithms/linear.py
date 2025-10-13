def find_element(arr, target):
    """
    Perform a linear search to find the index of the target element in the array.

    Parameters:
    arr (list): The list to search through.
    target: The element to search for.

    Returns:
    int: The index of the target element if found, otherwise -1.
    """
    for index in range(len(arr)):
        if arr[index] == target:
            return index
    return -1
# Example usage:
arr = [4, 2, 3, 5, 1]
target = 5
result = find_element(arr, target)
print(f"Element {target} found at index: {result}")  # Output: Element

target = 10
result = find_element(arr, target)
print("Element " + str(target) + " found at index: " + str(result) ) # Output: Element 5 found at index: 3