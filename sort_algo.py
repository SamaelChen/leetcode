# %%
class SortAlgo:
    def bubble_sort(self, arr):
        #冒泡法
        if len(arr) < 2:
            return arr
        for i in range(len(arr) - 1):
            flag = False
            for j in range(len(arr) - i - 1):
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
                    flag = True
            if not flag:
                break
        return arr
    
    def selection_sort(self, arr):
        # 选择排序
        if len(arr) < 2:
            return arr
        min_idx = 0
        while min_idx < len(arr):
            curr_min = float('inf')
            resume = arr[min_idx:]
            for i in range(len(resume)):
                if curr_min > resume[i]:
                    curr_min = resume[i]
                    idx = i + min_idx
            arr[min_idx], arr[idx] = arr[idx], arr[min_idx]
            min_idx += 1
        return arr
                
# %%
s = SortAlgo()
print(s.bubble_sort([5, 3, 4, 2, 1]))
print(s.selection_sort([5, 3, 4, 2, 1]))
# %%
