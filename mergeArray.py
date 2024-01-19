def arrayPairSum(nums):
    # Sort the array
    nums.sort()
    
    # Sum the minimums from each pair
    result_sum = sum(nums[::2])
    
    return result_sum
print(arrayPairSum([1,2,3,4,5,6,7,8,9]))