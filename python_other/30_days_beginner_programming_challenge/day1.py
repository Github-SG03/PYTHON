#####################################################Day1[challenge]:Alternates in an Array########################################################
# Problem Statement:You are given an array arr[], the task is to return a list elements of arr in alternate order (starting from index 0)
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



#####################################################Day1[Assignments]:Count Odd and Even########################################################
#Problem Statement:Given an array arr[] of positive integers. The task is to return the count of the number of odd and even elements in the array.
#Note: Return two elements where the first one in the count of odd & second one is the count of even.
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
