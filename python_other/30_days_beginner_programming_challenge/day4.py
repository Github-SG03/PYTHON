######################################################Day4[Problem Statement]########################################################
#https://www.youtube.com/redirect?event=video_description&redir_token=QUFFLUhqbjNpUTZycGdUdGF3Y0ZROWhkeXlpdWxoZzlLd3xBQ3Jtc0trUzlVd3FQWEtZLUE2ZnMzYzlJZmVRbnZPMTZBemNzY2FXV2RqcXBuUllLekZJRlZMSjZZc25aWm1MWWNDS3dfN0JpZ0Q4NzZwbU5TZmdqczllcExjdU9UQWZpOWtTRzV5OHQwbEhUVHAtU0NpUUNUdw&q=https%3A%2F%2Fwww.geeksforgeeks.org%2Fproblems%2Ffind-the-camel3348%2F0&v=ac2x4QXg-48##
#User function Template for python3
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
    
    
                
#{ 
 # Driver Code Starts
#Initial Template for Python 3

t = int (input ())
for tc in range (t):
    s = input ()
    ob = Solution()
    res = ob.count (s)
    
    for i in res:
        print (i)
    
    print("~")
# Contributed By: Pranay Bansal






#######################################################Day3[Assignments]########################################################
#https://www.youtube.com/redirect?event=video_description&redir_token=QUFFLUhqa0tuN25IV2FsRmtmalNBT3BRdkN1ZDJ2cGd4d3xBQ3Jtc0tuREpLLUZyWlNMZnFjdV9wQlF5b3czZEExZjJUUEM1c3FWTm1FdjB0YVkyTGdGVVhSWE0ycTlWWTJDcE9CMjluTFlkTEFoR3lCeDBoWVlNUWtYd0kwSVpMTWFIQUp6Q0hKd2ZtSkNXeXJwNmRSRWp1SQ&q=https%3A%2F%2Fwww.geeksforgeeks.org%2Fproblems%2Fcount-type-of-characters3635%2F0&v=ac2x4QXg-48
#User function Template for python3
class Solution:
    def countCamelCase (self,s):
        # your code here
        humps =0
        for char in s:
            if char.isupper():
                humps=humps+1
        return humps


#{ 
 # Driver Code Starts
#Initial Template for Python 3

t = int (input ())
for tc in range (t):
    s = input ()
    ob = Solution()
    print (ob.countCamelCase (s))

    print("~")
# Contributed By: Pranay Bansal

# } Driver Code Ends
# } Driver Code Ends#https://www.youtube.com/redirect?event=video_description&redir_token=QUFFLUhqbjNpUTZycGdUdGF3Y0ZROWhkeXlpdWxoZzlLd3xBQ3Jtc0trUzlVd3FQWEtZLUE2ZnMzYzlJZmVRbnZPMTZBemNzY2FXV2RqcXBuUllLekZJRlZMSjZZc25aWm1MWWNDS3dfN0JpZ0Q4NzZwbU5TZmdqczllcExjdU9UQWZpOWtTRzV5OHQwbEhUVHAtU0NpUUNUdw&q=https%3A%2F%2Fwww.geeksforgeeks.org%2Fproblems%2Ffind-the-camel3348%2F0&v=ac2x4QXg-48https://www.youtube.com/redirect?event=video_description&redir_token=QUFFLUhqbjNpUTZycGdUdGF3Y0ZROWhkeXlpdWxoZzlLd3xBQ3Jtc0trUzlVd3FQWEtZLUE2ZnMzYzlJZmVRbnZPMTZBemNzY2FXV2RqcXBuUllLekZJRlZMSjZZc25aWm1MWWNDS3dfN0JpZ0Q4NzZwbU5TZmdqczllcExjdU9UQWZpOWtTRzV5OHQwbEhUVHAtU0NpUUNUdw&q=https%3A%2F%2Fwww.geeksforgeeks.org%2Fproblems%2Ffind-the-camel3348%2F0&v=ac2x4QXg-48what are the predefeind string funtion in python??