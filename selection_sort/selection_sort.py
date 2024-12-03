#!/usr/bin/env python3
from typing import List

def selection_sort(nums: List[int]) -> List[int]:
    for i in range(0, len(nums)):
        min = i

        for j in range(i+1, len(nums)):
            if nums[j] < nums[min]:
                min = j
        
        nums[i], nums[min] = nums[min], nums[i]
    
    return nums

if __name__ == "__main__":
    nums_list=[5, 2, 4, 6, 1, 3]
    print(selection_sort(nums_list))