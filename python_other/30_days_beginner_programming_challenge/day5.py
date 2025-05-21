######################################################Day5[Problem Statement]########################################################
#https:https://www.youtube.com/redirect?event=video_description&redir_token=QUFFLUhqa21uYnVBdWI3LTZhU3VJakVJaEdsSHZKWGNMUXxBQ3Jtc0ttaWszVjhlYkdtd2NraWtkLTRSZ25JQzYtaWd1SHhsb3hFMWdzVG9LSXcxZjZOdHhfdHViaTBQNzVQRmJXXzljVnJEeFJEcTBjMVl6SlFOQVRlQnRsYmo0TUxhcl9jd3RhQlR0aW1CRWg0M290b2RMTQ&q=https%3A%2F%2Fwww.geeksforgeeks.org%2Fproblems%2Flargest-element-in-array4009%2F0&v=fwn9902r32s
from typing import List
class Solution:
    def largest(self, arr):
        # code here
        result=float('-inf')
        for num in arr:
            if num>result:
                result=num
            else:
                continue
        return result
    

#{ 
 # Driver Code Starts
#Initial Template for Python 3

t = int (input ())
arr=[]
for tc in range (t):
    s = int(input ())
    arr[tc].append(s)
       
ob = Solution()
res = ob.largest(arr)
print(res)
 
# Driver Code ends here
#}





########################################################Day5[Assignments]########################################################
#https://www.youtube.com/redirect?event=video_description&redir_token=QUFFLUhqbE5YTUFUOVFYdHVzeUdjV3BJc3N5eTdhWkpQUXxBQ3Jtc0ttbDF5ZnZvRExUcUtsSmxLT3VJZm9tUWp0V21NYnV0bFVHUGM2MU5UQjlWSHRvSXU4Nk9mTUg0NXRtVWlPcF96YlplR3A2U3cxNEM5UmF2WWJjSFVCeWt3Ul8yLVQzenRSTXd6TUhpbHBVVURXOUx1UQ&q=https%3A%2F%2Fwww.geeksforgeeks.org%2Fproblems%2Fsearching-a-number0324%2F0&v=fwn9902r32s
from typing import List
class Solution:
    def search(self, k: int, arr: List[int]) -> int:
        # code here
        for i in range(len(arr)):
            if arr[i] == k:
                return i + 1  # 1-based indexing
                
        return -1
    

#{ 
 # Driver Code Starts
#Initial Template for Python 3

t = int (input ())
arr=[]
for tc in range (t):
    s = int(input ())
    arr[tc].append(s)
       
ob = Solution()
res = ob.largest(arr)
print(res)
 







