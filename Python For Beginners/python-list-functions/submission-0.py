from typing import List # this is used to add type hints for List type

def get_sum(nums: List[int]) -> int:
    count = 0
    for i in nums:
        count += i
    return count
    
def get_min(nums: List[int]) -> int:
    current_minimum = nums[0]
    for i in nums:
        if (i < current_minimum):
            current_minimum = i
    return current_minimum
    
def get_max(nums: List[int]) -> int:
    current_max = nums[0]
    for i in nums:
        if (i > current_max):
            current_max = i
    return current_max

# do not modify below this line
print(get_sum([1, 2, 3, 4, 5]))
print(get_sum([5, 4, 5, 6]))

print(get_min([7, 3, 4, 5]))
print(get_min([5, 4, 5, 6]))

print(get_max([7, 3, 4, 5]))
print(get_max([5, 4, 5, 6]))
