"""
You are given a list of integers the represents the length of rods. 
You have to find out 2 largest rod of same length, if not possible the  return 0.
You can weld multiple rods.

Ex1:
arr=[2,4,3,6]
Output: 6
Explaination: we can find 2 rods of length 6. One is given another is weld 2 and 4.

Ex2:
arr=[5,4,3,6]
Output: 9
Explaination: we can find 2 rods of length 9. One is 5+4 andother is weld 3+6.
"""


def find_max_equal_rods(arr):
    n = len(arr)
    possible_sums = {}
    
    # Generate all possible combinations of 1 or more rods
    for i in range(1, 1 << n):
        current_sum = 0
        used_indices = set()
        for j in range(n):
            if i & (1 << j):
                current_sum += arr[j]
                used_indices.add(j)
        
        # Store the sum and the indices used to form it
        if current_sum not in possible_sums:
            possible_sums[current_sum] = []
        possible_sums[current_sum].append(used_indices)
    
    # Find the maximum sum that can be formed twice using different elements
    max_sum = 0
    for sum_val, combinations in possible_sums.items():
        if len(combinations) >= 2:
            # Check if we can form this sum twice using different elements
            for i in range(len(combinations)):
                for j in range(i + 1, len(combinations)):
                    # If the combinations don't share any elements
                    if not combinations[i].intersection(combinations[j]):
                        max_sum = max(max_sum, sum_val)
    
    return max_sum

# Test cases
def test_rod_welding():
    # Test case 1
    arr1 = [2, 4, 3, 6]
    print(f"Test case 1: {arr1}")
    result1 = find_max_equal_rods(arr1)
    print(f"Output: {result1}")  # Should output 6 (6 and 2+4)
    
    # Test case 2
    arr2 = [5, 4, 3, 6]
    print(f"Test case 2: {arr2}")
    result2 = find_max_equal_rods(arr2)
    print(f"Output: {result2}")  # Should output 9 (5+4 and 3+6)
    
    # Additional test case
    arr3 = [1, 2, 3, 4, 2]
    print(f"Test case 3: {arr3}")
    result3 = find_max_equal_rods(arr3)
    print(f"Output: {result3}")  # Should output 4 (4 and 2+2)

test_rod_welding()