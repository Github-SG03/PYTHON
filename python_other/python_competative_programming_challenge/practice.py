##############################################********PYTHON COMPETATIVE PROGRAMMING CHALLENGE*********#################################################
#####################################################Day1[Problem Statement]########################################################
#https://www.youtube.com/redirect?event=video_description&redir_token=QUFFLUhqbFJoYTAxcjV3Q2RnQWJQSTRHOGFFc01oenZMUXxBQ3Jtc0trYlF1LS1fM3hhTUJXeURPODhmbW93MjZhcld5bTZuTHFSb3Y1QWVKVzBCTG50QjVQM191b3F0VHdsdnR5RkpQdnpiUmV1NWlZcDIxNzk2QlZ1VGxRc0xJcVV6SmwzOE1BSDY3aXJ1RjdvNld0OFZORQ&q=https%3A%2F%2Fwww.geeksforgeeks.org%2Fproblems%2Fprint-alternate-elements-of-an-array%2F1%3Fpage%3D1%26category%3DArrays%26difficulty%3DBasic%26sortBy%3Dsubmissions&v=rsubrskHQ4s# Problem Statement:You are given an array arr[], the task is to return a list elements of arr in alternate order (starting from index 0
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



t = int(input())
for i in range(t):
    arr = list(map(int, input().split()))
    ls = Solution().getAlternates(arr)
    print(" ".join(map(str, ls)))
    print("~")
#https://www.youtube.com/redirect?event=video_description&redir_token=QUFFLUhqbTJJNDJCYzlObnBTeUxreF8waGd0TUYwSU1jd3xBQ3Jtc0tsY2hoTzRrVTFiSnFUU1huVFRpSXU4TjI2WkJ0b3pmemprdXNXbndmWERIeGNwR0tGZHBQUjNFZ190MFRCMEEzbllMWXBuRHZmNHZoQVdibkdUY05ud2xad0pjU2ZNbGZudFRnRDhKc2p4c0RfRnpENA&q=https%3A%2F%2Fwww.geeksforgeeks.org%2Fproblems%2Fcount-odd-even%2F0&v=rsubrskHQ4s
class Solution:
    def countOddEven(self, arr):
        odd = 0
        even = 0
        for number in arr:
            if number % 2 == 0:
                even = even + 1
            else:
                odd = odd + 1
        return odd, even



if __name__ == "__main__":
    # Testcase input
    testcase = int(input())
    for i in range(testcase):
        arr = list(map(int, input().split()))
        ob = Solution()
        res = ob.countOddEven(arr)
        print(*res)
        print("~")
#####################################################Day2#######################################################################
#[Problem Statement]:https://www.youtube.com/redirect?event=video_description&redir_token=QUFFLUhqbVA4bkE2OVNjWEljenUwM1BqSm9LdUlNNUJxZ3xBQ3Jtc0trMlFUanFxMFEzRk10Ukotb2xfazJVek9uS1pmUWxVaXd1dzlWaF9HeE5ScmtfaGw5WkxBVlhNM0RpdVNNRVFycWN6eWVlckIyNUpqYzVZdndpYUpyZDhVdEJkREMwMkx5bkFWNVNBaWRPRGtfMUtwbw&q=https%3A%2F%2Fwww.geeksforgeeks.org%2Fproblems%2Freplace-all-0s-with-5%2F0&v=3b34ZOgT2A4
class Solution:
    def convertFive(self, n):
        # Code here
        num_string = str(n)
        result_string=''
        for char in num_string:
            if char=='0':
                result_string=result_string+'5'
            else:
                result_string=result_string+char
        return result_string
        


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        ob = Solution()
        print(ob.convertFive(int(input().strip())))
        print("~")
#[Assignments1]:https://www.youtube.com/redirect?event=video_description&redir_token=QUFFLUhqa0hJTFNtR0Y3VW9YUkFwYzc5UjZsTUF1bHZqQXxBQ3Jtc0trTVlESHhGQThBSzNpWDNJODZETVY5M1FFVFVPNzBlLWVkUl91RlpvYmZUT1NlYk1ramRmRmMzMWw2ZlpfaUhSRjdlX1ZDWVNZZ1J3QXVSYXJUdXpSWUhnMXkwUktPeHU2RmZveWxRZzIyWlVDQ0ZuYw&q=https%3A%2F%2Fwww.geeksforgeeks.org%2Fproblems%2Fchange-the-string3541%2F0&v=3b34ZOgT2A4
class Solution:
    def conCat(self,s1,s2):
        # code here
        concat_string = s1 + s2
        return concat_string


if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        s1 = input()
        s2 = input()
        solObj = Solution()
        print(solObj.conCat(s1,s2))
#[Assignments2]:https://www.youtube.com/redirect?event=video_description&redir_token=QUFFLUhqbVA4bkE2OVNjWEljenUwM1BqSm9LdUlNNUJxZ3xBQ3Jtc0trMlFUanFxMFEzRk10Ukotb2xfazJVek9uS1pmUWxVaXd1dzlWaF9HeE5ScmtfaGw5WkxBVlhNM0RpdVNNRVFycWN6eWVlckIyNUpqYzVZdndpYUpyZDhVdEJkREMwMkx5bkFWNVNBaWRPRGtfMUtwbw&q=https%3A%2F%2Fwww.geeksforgeeks.org%2Fproblems%2Freplace-all-0s-with-5%2F0&v=3b34ZOgT2A4
class Solution:
    def modify(self, s):
        # code here
        if s[0].islower():
            return s.lower()
        else:
            return s.upper()
    
        

t = int (input ())
for tc in range (t):
    s = input ()
    ob = Solution()
    print(ob.modify(s))
######################################################Day3######################################################################
#[Problem Statement]:https://www.youtube.com/redirect?event=video_description&redir_token=QUFFLUhqbjQwWjBRbzBCMUhYaUhSR3pXN1otZVNBUjFEZ3xBQ3Jtc0tuYWpLUEJJZmxzSjRmTlFTOTZoZlNQUllueUtWZG5QYUxRZmQ4QnhheDlfQnFsOFZ1eHVDbUp0UEZHUG5vN19EQkpQM2NMNDhTQ2RCTlBaa0UwczFtZ3RTaGhQNHZPNEs0bDZWVl9KLXItTUQwbnkwNA&q=https%3A%2F%2Fwww.geeksforgeeks.org%2Fproblems%2Fsum-of-series2811%2F0&v=qC9FFshDvHwhttps://www.youtube.com/redirect?event=video_description&redir_token=QUFFLUhqbjQwWjBRbzBCMUhYaUhSR3pXN1otZVNBUjFEZ3xBQ3Jtc0tuYWpLUEJJZmxzSjRmTlFTOTZoZlNQUllueUtWZG5QYUxRZmQ4QnhheDlfQnFsOFZ1eHVDbUp0UEZHUG5vN19EQkpQM2NMNDhTQ2RCTlBaa0UwczFtZ3RTaGhQNHZPNEs0bDZWVl9KLXItTUQwbnkwNA&q=https%3A%2F%2Fwww.geeksforgeeks.org%2Fproblems%2Fsum-of-series2811%2F0&v=qC9FFshDvHwhttps://www.youtube.com/redirect?event=video_description&redir_token=QUFFLUhqbjQwWjBRbzBCMUhYaUhSR3pXN1otZVNBUjFEZ3xBQ3Jtc0tuYWpLUEJJZmxzSjRmTlFTOTZoZlNQUllueUtWZG5QYUxRZmQ4QnhheDlfQnFsOFZ1eHVDbUp0UEZHUG5vN19EQkpQM2NMNDhTQ2RCTlBaa0UwczFtZ3RTaGhQNHZPNEs0bDZWVl9KLXItTUQwbnkwNA&q=https%3A%2F%2Fwww.geeksforgeeks.org%2Fproblems%2Fsum-of-series2811%2F0&v=qC9FFshDvHwhttps://www.youtube.com/redirect?event=video_description&redir_token=QUFFLUhqbjQwWjBRbzBCMUhYaUhSR3pXN1otZVNBUjFEZ3xBQ3Jtc0tuYWpLUEJJZmxzSjRmTlFTOTZoZlNQUllueUtWZG5QYUxRZmQ4QnhheDlfQnFsOFZ1eHVDbUp0UEZHUG5vN19EQkpQM2NMNDhTQ2RCTlBaa0UwczFtZ3RTaGhQNHZPNEs0bDZWVl9KLXItTUQwbnkwNA&q=https%3A%2F%2Fwww.geeksforgeeks.org%2Fproblems%2Fsum-of-series2811%2F0&v=qC9FFshDvHw//www.youtube.com/redirect?event=video_description&redir_token=QUFFLUhqbjQwWjBRbzBCMUhYaUhSR3pXN1otZVNBUjFEZ3xBQ3Jtc0tuYWpLUEJJZmxzSjRmTlFTOTZoZlNQUllueUtWZG5QYUxRZmQ4QnhheDlfQnFsOFZ1eHVDbUp0UEZHUG5vN19EQkpQM2NMNDhTQ2RCTlBaa0UwczFtZ3RTaGhQNHZPNEs0bDZWVl9KLXItTUQwbnkwNA&q=https%3A%2F%2Fwww.geeksforgeeks.org%2Fproblems%2Fsum-of-series2811%2F0&v=qC9FFshDvHw##
class Solution:
    def seriesSum(self, n : int) -> int:
        # code here
        sum=0
        for i in range(n+1):
            sum=sum+i
        return sum
        


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        obj = Solution()
        res = obj.seriesSum(n)
        print(res)
        print("~")
#[Assignments]:https://www.youtube.com/redirect?event=video_description&redir_token=QUFFLUhqazlMVXN4S1gxQW50bmZDMTlTMXZBNHpLMlI1UXxBQ3Jtc0tuQUVPcGN5blEzc1JjbG02czY2Z1pzczBFME5rWjlMTlJQdG1vOXpmUnVTV2JDVlJ5Qk9qSzM4T2RJU2pDSEx2VG5wTmZrZ2NINklsY1pEcDJzWjR4bzJQYXZOSFp2MWJQUGZwYjhkMWtjNDA3WDhDMA&q=https%3A%2F%2Fwww.geeksforgeeks.org%2Fproblems%2Fsum-of-array2326%2F0&v=qC9FFshDvHw
class Solution:
    def arraySum(self, arr):
        # code here
        sum = 0
        for num in arr:
            sum = sum + num
        return sum
   		


if __name__ == "__main__":
    tc = int(input())
    while tc > 0:
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.arraySum(arr)
        print(ans)
        tc = tc - 1
        print("~")
######################################################Day4#####################################################################
#[Problem Statement]:https://www.youtube.com/redirect?event=video_description&redir_token=QUFFLUhqbjNpUTZycGdUdGF3Y0ZROWhkeXlpdWxoZzlLd3xBQ3Jtc0trUzlVd3FQWEtZLUE2ZnMzYzlJZmVRbnZPMTZBemNzY2FXV2RqcXBuUllLekZJRlZMSjZZc25aWm1MWWNDS3dfN0JpZ0Q4NzZwbU5TZmdqczllcExjdU9UQWZpOWtTRzV5OHQwbEhUVHAtU0NpUUNUdw&q=https%3A%2F%2Fwww.geeksforgeeks.org%2Fproblems%2Ffind-the-camel3348%2F0&v=ac2x4QXg-48##
class Solution:
    def count (self,s):
        # your code here
        lower=0
        upper=0
        special=0
        numeric=0
        whitespace=0
        for char in s:
            if char.isupper():
                upper=upper+1
            elif char.islower():
                lower=lower+1
            elif char.isnumeric():
                numeric=numeric+1
            elif char.isspace():
                whitespace=whitespace+1
            else:
                special=special+1
        return upper,lower,numeric,special
    
    

t = int (input ())
for tc in range (t):
    s = input ()
    ob = Solution()
    res = ob.count (s)
    
    for i in res:
        print (i)
    
    print("~")
#[Assignments]:https://www.youtube.com/redirect?event=video_description&redir_token=QUFFLUhqa0tuN25IV2FsRmtmalNBT3BRdkN1ZDJ2cGd4d3xBQ3Jtc0tuREpLLUZyWlNMZnFjdV9wQlF5b3czZEExZjJUUEM1c3FWTm1FdjB0YVkyTGdGVVhSWE0ycTlWWTJDcE9CMjluTFlkTEFoR3lCeDBoWVlNUWtYd0kwSVpMTWFIQUp6Q0hKd2ZtSkNXeXJwNmRSRWp1SQ&q=https%3A%2F%2Fwww.geeksforgeeks.org%2Fproblems%2Fcount-type-of-characters3635%2F0&v=ac2x4QXg-48
class Solution:
    def countCamelCase (self,s):
        # your code here
        humps =0
        for char in s:
            if char.isupper():
                humps=humps+1
        return humps



t = int (input ())
for tc in range (t):
    s = input ()
    ob = Solution()
    print (ob.countCamelCase (s))
    print("~")
######################################################Day5##########################################################################
#[Problem Statement]:https:https://www.youtube.com/redirect?event=video_description&redir_token=QUFFLUhqa21uYnVBdWI3LTZhU3VJakVJaEdsSHZKWGNMUXxBQ3Jtc0ttaWszVjhlYkdtd2NraWtkLTRSZ25JQzYtaWd1SHhsb3hFMWdzVG9LSXcxZjZOdHhfdHViaTBQNzVQRmJXXzljVnJEeFJEcTBjMVl6SlFOQVRlQnRsYmo0TUxhcl9jd3RhQlR0aW1CRWg0M290b2RMTQ&q=https%3A%2F%2Fwww.geeksforgeeks.org%2Fproblems%2Flargest-element-in-array4009%2F0&v=fwn9902r32s
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



t = int (input ())
arr=[]
for tc in range (t):
    s = int(input ())
    arr[tc].append(s)
       
ob = Solution()
res = ob.largest(arr)
print(res)
#[Assignments]:https://www.youtube.com/redirect?event=video_description&redir_token=QUFFLUhqbE5YTUFUOVFYdHVzeUdjV3BJc3N5eTdhWkpQUXxBQ3Jtc0ttbDF5ZnZvRExUcUtsSmxLT3VJZm9tUWp0V21NYnV0bFVHUGM2MU5UQjlWSHRvSXU4Nk9mTUg0NXRtVWlPcF96YlplR3A2U3cxNEM5UmF2WWJjSFVCeWt3Ul8yLVQzenRSTXd6TUhpbHBVVURXOUx1UQ&q=https%3A%2F%2Fwww.geeksforgeeks.org%2Fproblems%2Fsearching-a-number0324%2F0&v=fwn9902r32s
from typing import List
class Solution:
    def search(self, k: int, arr: List[int]) -> int:
        # code here
        for i in range(len(arr)):
            if arr[i] == k:
                return i + 1  # 1-based indexing
                
        return -1



t = int (input ())
arr=[]
for tc in range (t):
    s = int(input ())
    arr[tc].append(s)
######################################################Day6#####################################################################
#[Problem Statement]:https://www.youtube.com/redirect?event=video_description&redir_token=QUFFLUhqbmNKU2p2YnBUbUNqdDc1cnpNTU1mWnFxcHAyUXxBQ3Jtc0tta0xFQVhJTFZIWklIWE9MaDNXZjNiVkYtcXBvRTJjdW9LQk1nWm9qYVFodnEyVGtIeUM0TkhUX3drQmJTU2JPU1VyX0FTOV9Sa2tKenVfU1dsNGVtYnR4ZnBGNk1YWmNETDlHZlBuemVPY3NoanY5aw&q=https%3A%2F%2Fwww.geeksforgeeks.org%2Fproblems%2Fcheck-if-a-string-is-isogram-or-not-1587115620%2F0&v=lkyfIVevg3s
class Solution:
    #Your code here
    #Function to check if a string is Isogram or not.
    def isIsogram(self,s):
        value1=''
        for i in range(len(s)):
            value1=s[i]
            for j in range(i+1,len(s)):
                value2=s[j]
                if value1==value2:
                    return False
                else:
                    continue
        return True
#[Assignments]:https://www.youtube.com/redirect?event=video_description&redir_token=QUFFLUhqbTV1RjNYdjNWeWZuQWZobS1lRFdpSGR6c29XZ3xBQ3Jtc0tuOHE4djFidUpwREVVZkNxYmdQRHRpbjBWVXZrSDNKQlljQ3FEb1lzQ0JwRldNRHJBM1RVRnlHbFFJRUpFYjZxRnhWLXRPZm5zMmRzUUpLQ0xLN3c3WWpqQlVPS2VoTFVEMVRBYWg0WjA3SmJaRGVhOA&q=https%3A%2F%2Fwww.geeksforgeeks.org%2Fproblems%2Fjava-delete-alternate-characters4036%2F0&v=lkyfIVevg3s
class Solution:
    def delAlternate (ob, S):
        # code here 
        S=S[::2]
        return S
        



######################################################Day7[Problem Statement]########################################################
#[Problem Statement]:https://www.youtube.com/redirect?event=video_description&redir_token=QUFFLUhqa2lJMUNBNTNockJKcENZcWVPd0draHkwSkVOZ3xBQ3Jtc0trOWxNRmc2QjRfVzJaLVRZNkU1UFRjUWY4eV9JTDZKY2hzNU4tNWhMNUE3cFBzc2hoei0tQUdSSS1XSHBsSzVBd29PcDdHMmFhSFZ3SUVXVGhuc3dFVFU1blZqcS01MFRYV0NHQVE1c29Mb0xvRFVsUQ&q=https%3A%2F%2Fwww.geeksforgeeks.org%2Fproblems%2Fprime-number2314%2F0&v=5mTsiek4uHk
class Solution:
    def isPrime(self, n):
        # code here
        start=2
        end=n//2
        for x in range(start,end):
            if n%x==0:
                return False
        return True
#[Assignments]:https://www.youtube.com/redirect?event=video_description&redir_token=QUFFLUhqbUoxRm9sSkNQMGxYQ2JhMUpTNzl2Q1U0UzB5d3xBQ3Jtc0tsYU1maXVUMER6M2hCOG9JSzZrRUdpak5kQVNSSTROWk5kLUZJTkJlOFNNXzRsUUJ0MkpNeTMyanY1bmVPRGpBTjNSRzNJVHpwVlFfWVNKN0lTcUh0WnZDS3ZYbnI0LWU4Wk41R1pWTU4zeEVlMzlZUQ&q=https%3A%2F%2Fwww.geeksforgeeks.org%2Fproblems%2Fswap-kth-elements5500%2F0&v=5mTsiek4uHk
class Solution:
    def swapKth(self, arr, k):
        # Code Here
       for i in range(len(arr)):
           if i==k:
               temp= arr[k-1]
               arr[k-1]= arr[-k]
               arr[-k]=temp




#######################################################Day8#####################################################################
#[Problem Statement]:https://www.youtube.com/redirect?event=video_description&redir_token=QUFFLUhqbGhXV3R3LUpuSDUwTGdhT045TWhOSEhsS3NYd3xBQ3Jtc0tuRW5sS2I4WDNfYU1FZnI3SUNsMVh4NHZLaXJ2Tkp5WGN2UTVzNXZJNVJuUlNRcXRRTzZ5Ym1BSlRDWjU5am82eXF6Z0J1SU1xYkMwR25oTnRuSFdvLUUtM0hURnVYaG9RQmVQT01IQzVhbkx2SG5sVQ&q=https%3A%2F%2Fwww.geeksforgeeks.org%2Fproblems%2Fjava-reverse-a-string0416%2F0&v=dG5kLPxZVPA
class Solution:
    def revStr (self, s : str) -> str :
        # code here 
        rev_string=''
        for i in range(len(s)-1,-1,-1):
            rev_string=rev_string+s[i]
        return rev_string

#[Assignemnts]:#https://www.youtube.com/redirect?event=video_description&redir_token=QUFFLUhqbVFRWGlaeVdOR1VCZU1fcWowN2otSFh1cWNrQXxBQ3Jtc0tsMDhhT1dxZ0lIWDBfU0I4VW0xR2lXUWViSzlpNVRaalJycGZlODJ4NThBQ3hwaDNpQWJWNnpvRm9seG41dXVMRnl6MUNQeXBrLUgtZGpBc19Sa3VTajR4Uy1LaVFqNXh2VGdMa0lvQXBpRTdob0xMZw&q=https%3A%2F%2Fwww.geeksforgeeks.org%2Fproblems%2Freverse-a-string%2F0&v=dG5kLPxZVPA
class Solution:
    def revStr (self, s : str) -> str :
        # code here 
        rev_string=''
        for i in range(len(s)-1,-1,-1):
            rev_string=rev_string+s[i]
        return rev_string



