def generate_subsets(nums):
    """
    Generate all subsets of a given list of numbers.
    :param nums: List of numbers
    :return: List of all subsets
    """
    def backtrack(start, path):
        subsets_list.append(path[:])
        for i in range(start, len(nums)):
            path.append(nums[i])
            backtrack(i + 1, path)
            path.pop()
    
    subsets_list = []
    backtrack(0, [])
    return subsets_list

if __name__ == "__main__":
    nums = [1, 2, 3]
    print("All subsets:", generate_subsets(nums))