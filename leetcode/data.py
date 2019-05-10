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
    total = len(nums1) + len(nums2)
    left = 0
    right = 0
    count = 0
    while left + right < total:
        l1 = 0
        l2 = 0
        p1 = int(len(nums1) / 2)
        p2 = int(len(nums2) / 2)
        r1 = int(len(nums1) - 1)
        r2 = int(len(nums2) - 1)
        p1_idx = bisect_left(nums2, nums1[p1])
        p2_idx = bisect_left(nums1, nums2[p2])
        print("p1={}, p2={}".format(p1, p2))
        print("p1_idx={}, p2_idx={}".format(p1_idx, p2_idx))
        if p1_idx > p2:
            left += ((p2_idx - 1) - l1 + p2 - 1 - l2)
            right += (r2 - (p1_idx + 1) + r1 - (p1 + 1))
            l1 = p2_idx
            r1 = p1
            l2 = p2
            r2 = p1_idx
        else:
            left += ((p1_idx - 1) - l2 + p1 - 1 - l1)
            right += (r1 - (p2_idx + 1) + r2 - (p2 + 1))
            l2 = p1_idx
            r2 = p2
            l1 = p1
            r1 = p2_idx
        print("nums1= {}".format(nums1))
        print("nums2= {}".format(nums2))
        print("left: {}, right: {}".format(left, right))
        nums1 = nums1[l1 - 1:r1 + 1]
        nums2 = nums2[l2 - 1:r2 + 1]
        count += 1
        if count >= 4:
            break


def main():
    list_a, list_b = generateData()
    print(findMedianSortedArrays(list_a, list_b))



if __name__ == '__main__':
    main()
