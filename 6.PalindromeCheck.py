def PalindromeCheck(s,start,end):
    if(start>=end):
        return 1
    if(s[start]!=s[end]):
        return 0
    return PalindromeCheck(s,start+1,end-1)

string1 = "malayulam"
start = 0
end = len(string1)-1
if(PalindromeCheck(string1,start,end)):
    print('Palindrome String')
else:
    print('Not Palindrome')
