#!/usr/bin/env python3
from typing import List

def insertion_sort(nums: List[int]) -> List[int]:
    for i in range(1, len(nums)):
        key = nums[i]
        j=i

        while j > 0 and key < nums[j-1]:
            nums[j] = nums[j-1]
            j-=1
        
        nums[j] = key
    
    return nums

if __name__ == "__main__":
    nums_list=[5, 2, 4, 6, 1, 3]
    print(insertion_sort(nums_list))