ans = []
def PowerSet(s,temp,index):
    if(len(s)==index):
        print(temp)
        ans.append(temp)
        return 
    
    # take 
    PowerSet(s,temp+s[index],index+1)
    # not take
    PowerSet(s,temp,index+1)
    
    return

s = 'abc'
temp = ''
index = 0
PowerSet(s,temp,index)
print(ans)
