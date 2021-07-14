# Least Larger
# Given an array of numbers and an index, return the index of the least number
# larger than the element at the given index, or -1 if there is no such index.
# Example:
# Input: ([4, 1, 3, 5, 6], 0 ) 
# Output: 3
# Input: ([4, 1, 3, 5, 6], 4)
# Output: -1

#Brandon's answer
def least(arr,n):
    d = enumerate(arr)
    num = arr[n]
    for i in range(arr[n], max(arr)):
        if num +1 in arr:
            return arr.index(num +1)
        else:
            num+=1
    return -1
print(least([4,1,3,5,6],0))