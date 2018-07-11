# coding:utf-8
"""
二分法：分成两个排序的数组，两个指针分别指向两个排序数组，两个数组的交界处分别为数组最大值及最小值。
修改查找旋转数组的最小值，增加了最小值索引位置的需求。
"""
def min_rotate_array(rotate_array):
    if not rotate_array:
        return None, None
    idx_left = 0
    idx_right = len(rotate_array)-1
    idx_mid = 0
    while rotate_array[idx_left] >= rotate_array[idx_right]:
        if idx_right-idx_left == 1:
            return rotate_array[idx_right], idx_right

        idx_mid = (idx_right + idx_left)/2

        if rotate_array[idx_mid] == rotate_array[idx_left] == rotate_array[idx_right]:
            min, min_idx = get_min(rotate_array[idx_left:idx_right])
            return min, min_idx+idx_left

        if rotate_array[idx_mid] >= rotate_array[idx_left]:
            idx_left = idx_mid
        elif rotate_array[idx_mid] <= rotate_array[idx_right]:
            idx_right = idx_mid

    return rotate_array[idx_mid], idx_mid


def get_min(array):
    min = array[0]
    idx = 0
    for i, elem in enumerate(array):
        if min >= elem:
            min = elem
            idx = i
    return min, idx
