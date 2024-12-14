def insertion_sort(arr):
    # 從第二個元素開始，因為第一個元素被認為是已排序的
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        # 將當前元素與已排序部分的元素逐一比較並插入到正確位置
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

# 測試插入排序
if __name__ == "__main__":
    arr = [12, 11, 13, 5, 6]
    print("Unsorted array:", arr)
    insertion_sort(arr)
    print("Sorted array:", arr)
