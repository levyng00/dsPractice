#Fin the min and maximum in an array

#using linear search
def LMinMax(arr):
    min=0
    max=0
    if len(arr)==1:
        min = arr[0]
        max = arr[0]
        return min,max
    
    if len(arr)>1:
        if arr[0]>arr[1]:
            max = arr[0]
            min = arr[1]
        else :
            max = arr[0]
            min = arr[1]
    for i in range(2,len(arr)):
        if arr[i]>max:
            max = arr[i]
        elif arr[i]<min:
            min = arr[i]
    return max,min
print(LMinMax([1,2,4,21,2,3,1,2,1]))
        
            
        
        


