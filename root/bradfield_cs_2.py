#!/usr/bin/env python3

'''
2 Range count
Started 1755
Finished 1826
'''

# For simplicity we only consider arrays of integers
# but it is relatively straightforward to extend to floats

from typing import List

def count_x_linear_scan(x: int, a: List[int]) -> int:
    # O(n) time complexity
    return len([1 for n in a if x == n])

def count_x_binary_search(x:int, a: List[int]) -> int:
    '''
    One pass finds the rightmost index of x
    One pass finds the leftmost index of x
    O(log(n)) time complexity
    Will throw a ValueError if either cannot be found
    '''
    leftmost_val = _find_leftmost(a, x)
    rightmost_val = _find_rightmost(a,x)
    return rightmost_val - leftmost_val + 1

def _generate_random_sorted_array(length: int) -> List[int]:
    import random
    return sorted([random.randrange(100) for _ in range(length)])

def _run_test_harness(num_trials: int=1):
    import random
    from timeit import default_timer as timer

    for length in [10**i for i in range(1,8)]:
        for i in range(num_trials):
            a = _generate_random_sorted_array(length)
            i = random.randrange(length)
            linear_start = timer()
            r1 = count_x_linear_scan(a[i], a)
            linear_end = timer()
            bs_start = timer()
            r2 = count_x_binary_search(a[i], a)
            bs_end = timer()
            assert(r1 == r2)
            print(f"Time taken for linear scan of length {length}: {linear_end - linear_start:.8f}.")
            print(f"Time taken for binary search of length {length}: {bs_end - bs_start:.8f}." )
'''
The following two functions were adapted from the Python documentation
'''

def _find_leftmost(a, x):
    import bisect
    'Locate the leftmost value exactly equal to x'
    # bisect_left finds the leftmost value exactly equal to x
    i = bisect.bisect_left(a, x)
    if i != len(a) and a[i] == x:
        return i
    raise ValueError

def _find_rightmost(a, x):
    import bisect
    'Find rightmost value exactly equal to x'
    # bisect_right finds the leftmost value that is greater than x
    i = bisect.bisect_right(a, x)
    if i and a[i-1] == x:
        return i-1
    raise ValueError

'''
On my machine, I get the following results:
Time taken for linear scan of length 10: 0.00000185.
Time taken for binary search of length 10: 0.00000300.
Time taken for linear scan of length 100: 0.00000318.
Time taken for binary search of length 100: 0.00000166.
Time taken for linear scan of length 1000: 0.00002211.
Time taken for binary search of length 1000: 0.00000238.
Time taken for linear scan of length 10000: 0.00021265.
Time taken for binary search of length 10000: 0.00000703.
Time taken for linear scan of length 100000: 0.00206741.
Time taken for binary search of length 100000: 0.00000659.
Time taken for linear scan of length 1000000: 0.02330020.
Time taken for binary search of length 1000000: 0.00001136.
Time taken for linear scan of length 10000000: 0.20438045.
Time taken for binary search of length 10000000: 0.00001813.
'''

_run_test_harness(1)
