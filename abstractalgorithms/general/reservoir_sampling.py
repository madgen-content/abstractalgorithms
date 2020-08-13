from random import randrange

# select n random items from a large stream of unknown length
# or from a resource that is too large to fit into memory
# you need only supply an iterator on that resource
def reservoir_sample(itr, n):
    # the buffer of randomly selected 'things'
    kept = []

    # the first n 'things' get in no matter what
    for _ in range(n): 
        kept.append(next(itr))
    
    # evaluate the stream until empty
    while (obj := next(itr, None)) is not None:
        n += 1
        rval = randrange(n+1)

        if rval < n:
            # if the 'thing' makes it in, 
            # replace one of the buffer items at random
            replace_index = randrange(n)
            kept[replace_index] = obj
    return kept

def example():
    number_stream = (randrange(101) for _ in range(1000))
    print(reservoir_sample(itr, 20))
    return
