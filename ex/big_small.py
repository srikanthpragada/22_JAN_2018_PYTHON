def big_small(nums):
    """
    Returns a tuple with biggest and smallest values in the given sequence
    :param
         nums:  Is an sequence (List,Tuple, Set)
    :return  :  A tuple with smallest, biggest values
    """
    return min(nums), max(nums)


nums = [50, 70, 80, 90, 44, 77]
values = (10, 20, 11, 5, 70)

print(big_small(nums))
print(big_small(values))

print(big_small.__doc__)
