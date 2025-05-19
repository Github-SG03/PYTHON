#####################################################Day1[Problem Statement]########################################################
#https://www.youtube.com/redirect?event=video_description&redir_token=QUFFLUhqbFJoYTAxcjV3Q2RnQWJQSTRHOGFFc01oenZMUXxBQ3Jtc0trYlF1LS1fM3hhTUJXeURPODhmbW93MjZhcld5bTZuTHFSb3Y1QWVKVzBCTG50QjVQM191b3F0VHdsdnR5RkpQdnpiUmV1NWlZcDIxNzk2QlZ1VGxRc0xJcVV6SmwzOE1BSDY3aXJ1RjdvNld0OFZORQ&q=https%3A%2F%2Fwww.geeksforgeeks.org%2Fproblems%2Fprint-alternate-elements-of-an-array%2F1%3Fpage%3D1%26category%3DArrays%26difficulty%3DBasic%26sortBy%3Dsubmissions&v=rsubrskHQ4s# Problem Statement:You are given an array arr[], the task is to return a list elements of arr in alternate order (starting from index 0)

#User function Template for python3
class Solution:
    def getAlternates(self, arr):
        # Code Here
        output=[]
        for i in range(len(arr)): 
            if i%2==0:
                output.append(arr[i])
            else:
                continue

        return output


#{ 
 # Driver Code Starts
#Initial Template for Python 3
t = int(input())
for i in range(t):
    arr = list(map(int, input().split()))
    ls = Solution().getAlternates(arr)
    print(" ".join(map(str, ls)))
    print("~")

# } Driver Code Ends



#####################################################Day1[Assignments]########################################################
#https://www.youtube.com/redirect?event=video_description&redir_token=QUFFLUhqbTJJNDJCYzlObnBTeUxreF8waGd0TUYwSU1jd3xBQ3Jtc0tsY2hoTzRrVTFiSnFUU1huVFRpSXU4TjI2WkJ0b3pmemprdXNXbndmWERIeGNwR0tGZHBQUjNFZ190MFRCMEEzbllMWXBuRHZmNHZoQVdibkdUY05ud2xad0pjU2ZNbGZudFRnRDhKc2p4c0RfRnpENA&q=https%3A%2F%2Fwww.geeksforgeeks.org%2Fproblems%2Fcount-odd-even%2F0&v=rsubrskHQ4s
#User function Template for python3
class Solution:
    def countOddEven(self, arr):
        #Code here
        odd = 0
        even = 0
        for number in arr:
            if number % 2 == 0:
                even = even + 1
            else:
                odd = odd + 1
        return odd, even


#{ 
 # Driver Code Starts
if __name__ == "__main__":
    # Testcase input
    testcase = int(input())

    for _ in range(testcase):

        arr = list(map(int, input().split()))

        # Creating an object of the Solution class
        ob = Solution()

        # Calling the function to count even and odd
        res = ob.countOddEven(arr)

        # Printing the result
        print(*res)
        print("~")

# } Driver Code Ends


