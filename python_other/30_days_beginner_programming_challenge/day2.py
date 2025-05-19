#####################################################Day2[Problem Statement]########################################################
#https://www.youtube.com/redirect?event=video_description&redir_token=QUFFLUhqbVA4bkE2OVNjWEljenUwM1BqSm9LdUlNNUJxZ3xBQ3Jtc0trMlFUanFxMFEzRk10Ukotb2xfazJVek9uS1pmUWxVaXd1dzlWaF9HeE5ScmtfaGw5WkxBVlhNM0RpdVNNRVFycWN6eWVlckIyNUpqYzVZdndpYUpyZDhVdEJkREMwMkx5bkFWNVNBaWRPRGtfMUtwbw&q=https%3A%2F%2Fwww.geeksforgeeks.org%2Fproblems%2Freplace-all-0s-with-5%2F0&v=3b34ZOgT2A4
# Function should return an integer value
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
        


#{ 
 # Driver Code Starts
if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        ob = Solution()
        print(ob.convertFive(int(input().strip())))
        print("~")
# } Driver Code Ends


#####################################################Day2[Assignmnets]########################################################
#1.https://www.youtube.com/redirect?event=video_description&redir_token=QUFFLUhqa0hJTFNtR0Y3VW9YUkFwYzc5UjZsTUF1bHZqQXxBQ3Jtc0trTVlESHhGQThBSzNpWDNJODZETVY5M1FFVFVPNzBlLWVkUl91RlpvYmZUT1NlYk1ramRmRmMzMWw2ZlpfaUhSRjdlX1ZDWVNZZ1J3QXVSYXJUdXpSWUhnMXkwUktPeHU2RmZveWxRZzIyWlVDQ0ZuYw&q=https%3A%2F%2Fwww.geeksforgeeks.org%2Fproblems%2Fchange-the-string3541%2F0&v=3b34ZOgT2A4
#User function Template for python3
class Solution:

    def conCat(self,s1,s2):
        # code here
        concat_string = s1 + s2
        return concat_string



#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

    t = int(input())

    for _ in range(t):
        s1 = input()
        s2 = input()

        solObj = Solution()

        print(solObj.conCat(s1,s2))
# } Driver Code Ends










#2.https://www.youtube.com/redirect?event=video_description&redir_token=QUFFLUhqbVA4bkE2OVNjWEljenUwM1BqSm9LdUlNNUJxZ3xBQ3Jtc0trMlFUanFxMFEzRk10Ukotb2xfazJVek9uS1pmUWxVaXd1dzlWaF9HeE5ScmtfaGw5WkxBVlhNM0RpdVNNRVFycWN6eWVlckIyNUpqYzVZdndpYUpyZDhVdEJkREMwMkx5bkFWNVNBaWRPRGtfMUtwbw&q=https%3A%2F%2Fwww.geeksforgeeks.org%2Fproblems%2Freplace-all-0s-with-5%2F0&v=3b34ZOgT2A4
#User function Template for python3
class Solution:
    def modify(self, s):
        # code here
        if s[0].islower():
            return s.lower()
        else:
            return s.upper()
    
        
#{ 
 # Driver Code Starts
#Initial Template for Python 3

t = int (input ())
for tc in range (t):
    s = input ()
    ob = Solution()
    print(ob.modify(s))
# } Driver Code Ends###############################################Day2[Assignments]######################################################://www.youtube.com/redirect?event=video_description&redir_token=QUFFLUhqa0hJTFNtR0Y3VW9YUkFwYzc5UjZsTUF1bHZqQXxBQ3Jtc0trTVlESHhGQThBSzNpWDNJODZETVY5M1FFVFVPNzBlLWVkUl91RlpvYmZUT1NlYk1ramRmRmMzMWw2ZlpfaUhSRjdlX1ZDWVNZZ1J3QXVSYXJUdXpSWUhnMXkwUktPeHU2RmZveWxRZzIyWlVDQ0ZuYw&q=https%3A%2F%2Fwww.geeksforgeeks.org%2Fproblems%2Fchange-the-string3541%2F0&v=3b34ZOgT2A4uuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuu