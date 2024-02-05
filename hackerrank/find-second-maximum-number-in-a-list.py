if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    
    max_num = max(arr)
    arr_without_max = [i for i in arr if i != max_num]
    runner_up = max(arr_without_max)
    
    print(runner_up)
