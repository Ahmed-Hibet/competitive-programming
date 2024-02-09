#User function Template for python3

class Solution:
    #Function to check if two arrays are equal or not.
    def check(self,A,B,N):
        
        #return: True or False
        
        count = {}
        
        for num in A:
            count[num] = count.get(num, 0) + 1
            
        for num in B:
            remain = count.get(num, 0)
            if remain == 0:
                return 0
                
            count[num] -= 1
            
        for value in count.values():
            if value != 0:
                return 0
                
        return 1


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=='__main__':
    t=int(input())
    for tc in range(t):
        
        N=int(input())
        
        A = [int(x) for x in input().replace('  ',' ').strip().split(' ')]
        B = [int(x) for x in input().replace('  ',' ').strip().split(' ')]
        ob=Solution()
        if ob.check(A,B,N):
            print(1)
        else:
            print(0)
        
                
                
# } Driver Code Ends
