######################################################Day7[Problem Statement]########################################################
#https://www.youtube.com/redirect?event=video_description&redir_token=QUFFLUhqa2lJMUNBNTNockJKcENZcWVPd0draHkwSkVOZ3xBQ3Jtc0trOWxNRmc2QjRfVzJaLVRZNkU1UFRjUWY4eV9JTDZKY2hzNU4tNWhMNUE3cFBzc2hoei0tQUdSSS1XSHBsSzVBd29PcDdHMmFhSFZ3SUVXVGhuc3dFVFU1blZqcS01MFRYV0NHQVE1c29Mb0xvRFVsUQ&q=https%3A%2F%2Fwww.geeksforgeeks.org%2Fproblems%2Fprime-number2314%2F0&v=5mTsiek4uHk



class Solution:
    def isPrime(self, n):
        # code here
        start=2
        end=n//2
        for x in range(start,end):
            if n%x==0:
                return False
        return True
    








#########################################################Day7[Assignments]########################################################
#https://www.youtube.com/redirect?event=video_description&redir_token=QUFFLUhqbUoxRm9sSkNQMGxYQ2JhMUpTNzl2Q1U0UzB5d3xBQ3Jtc0tsYU1maXVUMER6M2hCOG9JSzZrRUdpak5kQVNSSTROWk5kLUZJTkJlOFNNXzRsUUJ0MkpNeTMyanY1bmVPRGpBTjNSRzNJVHpwVlFfWVNKN0lTcUh0WnZDS3ZYbnI0LWU4Wk41R1pWTU4zeEVlMzlZUQ&q=https%3A%2F%2Fwww.geeksforgeeks.org%2Fproblems%2Fswap-kth-elements5500%2F0&v=5mTsiek4uHk

class Solution:
    def swapKth(self, arr, k):
        # Code Here
       for i in range(len(arr)):
           if i==k:
               temp= arr[k-1]
               arr[k-1]= arr[-k]
               arr[-k]=temp
       return