def revArray(arr,start,end):
    if(start>=end):
        return arr
    temp = arr[start]
    arr[start] = arr[end]
    arr[end] = temp
    return revArray(arr,start+1,end-1)

arr = [1,2,3,4,5]
start = 0
end = len(arr) - 1
print(revArray(arr,start,end))
