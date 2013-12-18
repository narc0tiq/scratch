
a = [12, 3, 44, 98, 4, 59, 85]

def merge_sort(a):
    if len(a) <= 1:
        print '%r is sorted' % a
        return a

    midpoint = len(a)/2
    left = a[0:midpoint]
    right = a[midpoint:len(a)]

    print "%r: split into %r and %r" % (a, left, right)

    left = merge_sort(left)
    right = merge_sort(right)

    return merge(left, right)


def merge(left, right):
    result = []
    print '%r and %r: merge to' % (left, right),

    while left or right:
        if left and right:
            if left[0] <= right[0]:
                result.append(left[0])
                left = left[1:]
            else:
                result.append(right[0])
                right = right[1:]
        elif left:
            result.append(left[0])
            left = left[1:]
        elif right:
            result.append(right[0])
            right = right[1:]

    print result
    return result


if __name__ == '__main__':
    merge_sort(a)
