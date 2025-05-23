######################################################Day6[Problem Statement]########################################################
#https://www.youtube.com/redirect?event=video_description&redir_token=QUFFLUhqbmNKU2p2YnBUbUNqdDc1cnpNTU1mWnFxcHAyUXxBQ3Jtc0tta0xFQVhJTFZIWklIWE9MaDNXZjNiVkYtcXBvRTJjdW9LQk1nWm9qYVFodnEyVGtIeUM0TkhUX3drQmJTU2JPU1VyX0FTOV9Sa2tKenVfU1dsNGVtYnR4ZnBGNk1YWmNETDlHZlBuemVPY3NoanY5aw&q=https%3A%2F%2Fwww.geeksforgeeks.org%2Fproblems%2Fcheck-if-a-string-is-isogram-or-not-1587115620%2F0&v=lkyfIVevg3s
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
    


#########################################################Day6[Assignments]########################################################
#https://www.youtube.com/redirect?event=video_description&redir_token=QUFFLUhqbTV1RjNYdjNWeWZuQWZobS1lRFdpSGR6c29XZ3xBQ3Jtc0tuOHE4djFidUpwREVVZkNxYmdQRHRpbjBWVXZrSDNKQlljQ3FEb1lzQ0JwRldNRHJBM1RVRnlHbFFJRUpFYjZxRnhWLXRPZm5zMmRzUUpLQ0xLN3c3WWpqQlVPS2VoTFVEMVRBYWg0WjA3SmJaRGVhOA&q=https%3A%2F%2Fwww.geeksforgeeks.org%2Fproblems%2Fjava-delete-alternate-characters4036%2F0&v=lkyfIVevg3s
class Solution:
    def delAlternate (ob, S):
        # code here 
        S=S[::2]
        return S
        


        