'''
The count-and-say sequence is the sequence of integers with the first five terms as following:

1.     1
2.     11
3.     21
4.     1211
5.     111221
1 is read off as "one 1" or 11.
11 is read off as "two 1s" or 21.
21 is read off as "one 2, then one 1" or 1211.

Given an integer n where 1 ≤ n ≤ 30, generate the nth term of the count-and-say sequence. You can do so recursively, in other words from the previous member read off the digits, counting the number of digits in groups of the same digit.

Note: Each term of the sequence of integers will be represented as a string.

'''

class Solution:
    def countAndSay(self, n: int) -> str:
        ahead = "1"         
        if n == 1: 
            return ahead       
        else:
            for i in range(1,n):
                after = self.strcount(ahead)
                ahead = after
            return ahead
                                          
    def strcount(self,fd):           
        ct = 1
        ot = ""
        for i in range(1,len(fd)):
            if fd[i] == fd[i-1]:
                ct += 1
            else: 
                ot += (str(ct)+fd[i-1])
                ct = 1
        ot += str(ct)+fd[-1]
        return ot
