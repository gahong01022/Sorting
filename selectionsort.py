def selection_sort(arr):
    # 遍歷數列
    for i in range(len(arr)):
        # 假設當前元素是最小值
        min_idx = i
        # 找到未排序部分中的最小值
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        # 將找到的最小值與當前元素交換
        (arr[i], arr[min_idx]) = (arr[min_idx], arr[i])

# 測試選擇排序
if __name__ == "__main__":
    arr = [64, 25, 12, 22, 11]
    print("Unsorted array:", arr)
    selection_sort(arr)
    print("Sorted array:", arr)
