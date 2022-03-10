'''
Implement strStr().

Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

Example 1:

Input: haystack = "hello", needle = "ll"
Output: 2
Example 2:

Input: haystack = "aaaaa", needle = "bba"
Output: -1
'''

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:        
        needle_len = len(needle)                
        for i in range(len(haystack) - needle_len +1):          
            if haystack[i:(i+needle_len)] == needle:
                return i           
        return -1
