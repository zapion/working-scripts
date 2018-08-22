# -*- coding: utf-8 -*-


from bisect import bisect_left
import random


def generateData():
    la = []
    lb = []
    for i in range(100):
        flop = random.randint(0, 2)
        if flop == 0:
            la.append(i)
        else:
            lb.append(i)
    return (la, lb)


def findMedianSortedArrays(nums1, nums2):
    """
    :type nums1: List[int]
    :type nums2: List[int]
    :rtype: float
    """
    left = 0
    right = 0
    p1 = int(len(nums1) / 2)
    p2 = int(len(nums2) / 2)
    l1 = 0
    l2 = 0
    r1 = int(len(nums1) - 1)
    r2 = int(len(nums2) - 1)
    while left + right < len(nums1) + len(nums2):
        p1_idx = bisect_left(nums2, nums1[p1])
        p2_idx = bisect_left(nums1, nums2[p2])
        if p1_idx > p2:
            left += (p2_idx - l1 + p2 - l2)
            right += (r2 - p1_idx + r1 - p1)
            l1 = p2_idx
            r1 = p1
            l2 = p2
            r2 = p1_idx
        else:
            left += (p1_idx - l2 + p1 - l1)
            right += (r1 - p2_idx + r2 - p2)
            l2 = p1_idx
            r2 = p2
            l1 = p1
            r1 = p2_idx
        print("{}:::{}".format(left, right))
        break


def main():
    list_a, list_b = generateData()
    print(findMedianSortedArrays(list_a, list_b))



if __name__ == '__main__':
    main()
