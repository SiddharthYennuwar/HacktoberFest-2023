class Solution(object):
    def lengthOfLongestSubstring(self, s):
        if len(s) == 0:
          print(0)
        j,list1=0,[]                    
        for i in range(len(s)):
          if s[i] in s[j:i]:
            ind = s[j:i].index(s[i])
            j = ind + j +1         
          else:
            list1.append(i-j+1)
        if(len(list1)==0):
            return len(s)
        else:
            return max(list1)