def merge_sort(nums):
    if not nums:
        raise ValueError("Input array is empty")

    if len(nums) == 1:
        return nums

    mid = len(nums) // 2
    left = nums[:mid]
    right = nums[mid:]

    merge_sort(left)
    merge_sort(right)

    i = j = k = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            nums[k] = left[i]
            i += 1
        else:
            nums[k] = right[j]
            j += 1
        k += 1

    while i < len(left):
        nums[k] = left[i]
        i += 1
        k += 1

    while j < len(right):
        nums[k] = right[j]
        j += 1
        k += 1

    return nums


# Example usage:
try:
    nums = [4, 2, 1, 3, 5]
    sorted_nums = merge_sort(nums)
    print("Sorted array:", sorted_nums)
except ValueError as e:
    print(e)
