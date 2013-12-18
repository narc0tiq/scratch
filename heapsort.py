
a = [12, 3, 44, 98, 4, 59, 85]

def heapify(a):
    count = len(a)
    start = (count - 2) / 2

    while start >= 0:
        sift_down(a, start, count-1)
        start -= 1


def sift_down(a, start, end):
    root = start

    while 2*root + 1 <= end:
        child = 2*root + 1
        swap = root

        if a[swap] < a[child]:
            swap = child

        if child+1 <= end and a[swap] < a[child+1]:
            swap = child + 1

        if swap is not root:
            do_swap(a, root, swap, 'heapify')
            root = swap
        else:
            return


def heapsort(a):
    print "%r initial condition" % a
    heapify(a)

    end = len(a) - 1
    while end > 0:
        do_swap(a, 0, end, 'put the maximum at the end')
        end -= 1
        sift_down(a, 0, end)


def do_swap(a, left, right, note=''):
    a[left], a[right] = a[right], a[left]
    print "%r after swap(%d, %d): %s" % (a, left, right, note)


if __name__ == '__main__':
    heapsort(a)
