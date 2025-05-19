######################################################Day3[Problem Statement]########################################################
#https://www.youtube.com/redirect?event=video_description&redir_token=QUFFLUhqbjQwWjBRbzBCMUhYaUhSR3pXN1otZVNBUjFEZ3xBQ3Jtc0tuYWpLUEJJZmxzSjRmTlFTOTZoZlNQUllueUtWZG5QYUxRZmQ4QnhheDlfQnFsOFZ1eHVDbUp0UEZHUG5vN19EQkpQM2NMNDhTQ2RCTlBaa0UwczFtZ3RTaGhQNHZPNEs0bDZWVl9KLXItTUQwbnkwNA&q=https%3A%2F%2Fwww.geeksforgeeks.org%2Fproblems%2Fsum-of-series2811%2F0&v=qC9FFshDvHwhttps://www.youtube.com/redirect?event=video_description&redir_token=QUFFLUhqbjQwWjBRbzBCMUhYaUhSR3pXN1otZVNBUjFEZ3xBQ3Jtc0tuYWpLUEJJZmxzSjRmTlFTOTZoZlNQUllueUtWZG5QYUxRZmQ4QnhheDlfQnFsOFZ1eHVDbUp0UEZHUG5vN19EQkpQM2NMNDhTQ2RCTlBaa0UwczFtZ3RTaGhQNHZPNEs0bDZWVl9KLXItTUQwbnkwNA&q=https%3A%2F%2Fwww.geeksforgeeks.org%2Fproblems%2Fsum-of-series2811%2F0&v=qC9FFshDvHwhttps://www.youtube.com/redirect?event=video_description&redir_token=QUFFLUhqbjQwWjBRbzBCMUhYaUhSR3pXN1otZVNBUjFEZ3xBQ3Jtc0tuYWpLUEJJZmxzSjRmTlFTOTZoZlNQUllueUtWZG5QYUxRZmQ4QnhheDlfQnFsOFZ1eHVDbUp0UEZHUG5vN19EQkpQM2NMNDhTQ2RCTlBaa0UwczFtZ3RTaGhQNHZPNEs0bDZWVl9KLXItTUQwbnkwNA&q=https%3A%2F%2Fwww.geeksforgeeks.org%2Fproblems%2Fsum-of-series2811%2F0&v=qC9FFshDvHwhttps://www.youtube.com/redirect?event=video_description&redir_token=QUFFLUhqbjQwWjBRbzBCMUhYaUhSR3pXN1otZVNBUjFEZ3xBQ3Jtc0tuYWpLUEJJZmxzSjRmTlFTOTZoZlNQUllueUtWZG5QYUxRZmQ4QnhheDlfQnFsOFZ1eHVDbUp0UEZHUG5vN19EQkpQM2NMNDhTQ2RCTlBaa0UwczFtZ3RTaGhQNHZPNEs0bDZWVl9KLXItTUQwbnkwNA&q=https%3A%2F%2Fwww.geeksforgeeks.org%2Fproblems%2Fsum-of-series2811%2F0&v=qC9FFshDvHw//www.youtube.com/redirect?event=video_description&redir_token=QUFFLUhqbjQwWjBRbzBCMUhYaUhSR3pXN1otZVNBUjFEZ3xBQ3Jtc0tuYWpLUEJJZmxzSjRmTlFTOTZoZlNQUllueUtWZG5QYUxRZmQ4QnhheDlfQnFsOFZ1eHVDbUp0UEZHUG5vN19EQkpQM2NMNDhTQ2RCTlBaa0UwczFtZ3RTaGhQNHZPNEs0bDZWVl9KLXItTUQwbnkwNA&q=https%3A%2F%2Fwww.geeksforgeeks.org%2Fproblems%2Fsum-of-series2811%2F0&v=qC9FFshDvHw##

class Solution:
    def seriesSum(self, n : int) -> int:
        # code here
        sum=0
        for i in range(n+1):
            sum=sum+i
        return sum
        



#{ 
 # Driver Code Starts
if __name__ == '__main__':
    t = int(input())
    for _ in range(t):

        n = int(input())

        obj = Solution()
        res = obj.seriesSum(n)

        print(res)
        print("~")
######################################################Day3[Assignments]########################################################
#https://www.youtube.com/redirect?event=video_description&redir_token=QUFFLUhqazlMVXN4S1gxQW50bmZDMTlTMXZBNHpLMlI1UXxBQ3Jtc0tuQUVPcGN5blEzc1JjbG02czY2Z1pzczBFME5rWjlMTlJQdG1vOXpmUnVTV2JDVlJ5Qk9qSzM4T2RJU2pDSEx2VG5wTmZrZ2NINklsY1pEcDJzWjR4bzJQYXZOSFp2MWJQUGZwYjhkMWtjNDA3WDhDMA&q=https%3A%2F%2Fwww.geeksforgeeks.org%2Fproblems%2Fsum-of-array2326%2F0&v=qC9FFshDvHw
#User function Template for python3
class Solution:
    def arraySum(self, arr):
        # code here
        sum = 0
        for num in arr:
            sum = sum + num
        return sum
   		



#{ 
 # Driver Code Starts
# Driver code
if __name__ == "__main__":
    tc = int(input())
    while tc > 0:
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.arraySum(arr)
        print(ans)
        tc = tc - 1
        print("~")

# } Driver Code Ends