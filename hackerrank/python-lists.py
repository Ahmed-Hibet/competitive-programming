if __name__ == '__main__':
    arr = []
    
    N = int(input())
    for _ in range(N):
        command = input().split()
        
        if command[0] == 'insert':
            i = int(command[1])
            e = int(command[2])
            arr.insert(i, e)
        elif command[0] == 'print':
            print(arr)
        elif command[0] == 'remove':
            e = int(command[1])
            arr.remove(e)
        elif command[0] == 'append':
            e = int(command[1])
            arr.append(e)
        elif command[0] == 'sort':
            arr.sort()
        elif command[0] == 'pop':
            arr.pop()
        elif command[0] == 'reverse':
            arr.reverse()
        
        
