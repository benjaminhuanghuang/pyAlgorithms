# http://algorithmsandstuff.blogspot.com/2014/06/radix-sort-in-c-sharp.html
def radix_sort(nums):
    digitPosition = 0
    isFinished = False

    buckets = [[] for i in xrange(10)]
    while not isFinished:
        isFinished = True
        for num in nums:
            bucketNum = get_bucket_number(num, digitPosition)

            if bucketNum > 0:
                isFinished = False
            buckets[bucketNum].append(num)

        i = 0
        for bucket in buckets:
            while len(bucket) > 0:
                nums[i] = bucket.pop(0)
                i += 1
        digitPosition += 1

    return nums


def get_bucket_number(value, digitPos):
    return (value / (10 ** digitPos)) % 10


def radixsort(aList):
    RADIX = 10
    maxLength = False
    tmp, placement = -1, 1

    while not maxLength:
        maxLength = True
        # declare and initialize buckets
        buckets = [list() for _ in range(RADIX)]

        # split aList between lists
        for i in aList:
            tmp = i // placement
            print ("i is ", i)
            print ("placement is ", placement)
            print ("tmp is ", tmp)
            print ("tmp % RADIX is ", tmp % RADIX)
            buckets[tmp % RADIX].append(i)
            if maxLength and tmp > 0:
                maxLength = False

        # empty lists into aList array
        a = 0
        for b in range(RADIX):
            buck = buckets[b]
            for i in buck:
                aList[a] = i
                a += 1

        # move to next digit
        placement *= RADIX
    return aList


if __name__ == '__main__':
    nums = [97, 77, 377, 477, 7]
    res = radix_sort(nums)
    print res
