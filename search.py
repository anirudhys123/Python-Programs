def binary_search(arr, target):
    """
    Perform binary search on a sorted array to find the target element.
    :param arr: List of sorted elements
    :param target: Element to search for
    :return: Index of the target element if found, otherwise -1
    """
    if not arr:
        return -1  # Return -1 for empty array

    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = left + (right - left) // 2  # Avoid potential overflow
        
        if arr[mid] == target:
            return mid  # Target found
        elif arr[mid] < target:
            left = mid + 1  # Search in the right half
        else:
            right = mid - 1  # Search in the left half
    
    return -1  # Target not found

# Example usage
if __name__ == "__main__":
    sorted_list = [1, 3, 5, 7, 9, 11]
    target_value = 7
    result = binary_search(sorted_list, target_value)
    print(f"Target {target_value} found at index: {result}" if result != -1 else "Target not found")
