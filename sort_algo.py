# %%
import heapq


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
    
    def insertion_sort(self, arr):
        length = len(arr)
        if length < 2:
            return arr
        for i in range(1, length):
            j = i - 1
            while arr[i] < arr[j] and j >= 0:
                j -= 1
            arr.insert(j+1, arr[i])
            arr[i+1:] = arr[i+2:]
        return arr
            
    def shell_sort(self, arr):
        length = len(arr)
        if length < 2:
            return arr
        gap = length // 2
        while gap > 0:
            if gap == 1:
                arr = self.insertion_sort(arr)
            else:
                for i in range(length - gap):
                    if arr[i] > arr[i+gap]:
                        arr[i], arr[i+gap] = arr[i+gap], arr[i]
            gap = gap // 2
        return arr
# %%
s = SortAlgo()
print(s.bubble_sort([5, 3, 3, 4, 2, 1]))
print(s.selection_sort([5, 3, 3, 4, 2, 1]))
print(s.insertion_sort([2, 3, 4, 5, 3, 1]))
print(s.shell_sort([5, 3, 3, 4, 2, 1]))
# %%