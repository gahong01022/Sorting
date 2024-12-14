def bubble_sort(nums):
    n = len(nums)
    for i in range(n-1):
        for j in range(n-i-1):
            if nums[j] > nums[j+1]:
                temp = nums[j]
                nums[j] = nums[j+1]
                nums[j+1] = temp
            
nums = [3,2,4,5,1]
print("排序前 = %s" % nums)
bubble_sort(nums)
print("排序後 = %s" % nums)