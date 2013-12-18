
a = [12, 3, 44, 98, 4, 59, 85]


def quicksort(a, start=None, end=None):
    if start is None: start = 0
    if end is None: end = len(a) - 1

    print a, 'scanning', (start, end)
    if start >= end:
        return  # nothing to do

    pivot = end
    store = start

    for examine in xrange(start, end):
        if a[examine] <= a[pivot]:
            if examine != store:
                print a, 'swapping', (store, examine), (a[store], a[examine])
                a[examine], a[store] = a[store], a[examine]
            store += 1

    if pivot != store:
        print a, 'placing pivot, swapping', (store, pivot)
        a[pivot], a[store] = a[store], a[pivot]

    if store > start:
        quicksort(a, start, store - 1)
    if store < end:
        quicksort(a, store + 1, end)

if __name__ == '__main__':
    print a
    quicksort(a)
    print a
