class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        n = len(arr)
        result = []
        for i in range(n, 0, -1):
            index = arr.index(i)
            arr = arr[:index+1][::-1] + arr[index+1:]
            arr = arr[:i][::-1] + arr[i:]
            result.append(index+1)
            result.append(i)
        return result
