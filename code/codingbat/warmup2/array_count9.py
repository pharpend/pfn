def array_count9(nums):
    num_nines = 0
    for n in nums:
        if n == 9:
            num_nines = num_nines + 1
    return num_nines
