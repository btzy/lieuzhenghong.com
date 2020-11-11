#!/usr/bin/env python3

'''
4 Exponential backoff
1826
1912 but really was done at 1855
'''

import functools

def exp_backoff(fn,
                first_backoff: float,
                max_retries:int,
                jitter_min:int,
                jitter_max:int):
    '''
    Performs exponential backoff on a function `fn` up to max_retries times.
    Waits (first_backoff * 2**num_retries) + rand[jitter_min, jitter_max]
    seconds between each retry to prevent "thundering herd" effects. 

    Note that jitter_min can be a negative number, and
    (first_backoff + jitter_min) must > 0 in order to preserve
    the space-time continuum.

    Returns the result of the function,
    or raises an exception if all retries have been exhausted
    and the function has still failed.
    '''
    import random
    import time
    result = None
    num_retries = 0
    assert(first_backoff + jitter_min >= 0)
    while not result and num_retries < max_retries: 
        print("Calling function...")
        try:
            result = fn()
        except Exception as e: # not sure if this is a code smell
            print(e)
            print(f"Function failed {num_retries + 1} / {max_retries} times. Retrying...")
            jitter = random.uniform(jitter_min, jitter_max)
            time_to_wait = (first_backoff * 2**num_retries) + jitter
            print(f"Backing off for {time_to_wait} seconds...")
            time.sleep(time_to_wait)
            num_retries += 1
    if not result:
        raise Exception("Maximum number of retries reached")
    return result

def function_that_could_fail(p: float):
    import random
    if (random.uniform(0, 1) < p):
        print("Function succeeded!")
        return 1
    raise Exception("Function failed because I said so")


exp_backoff(functools.partial(function_that_could_fail, 0.15), 1, 5, -0.5, 0.5)
