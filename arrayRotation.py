def rotateArr(arr,d):
    temp=[]
    for i in range(d,len(arr)):
        temp.append(arr[i])
    for i in range(0,d):
        temp.append(arr[i])
    print(temp)
rotateArr([1,2,3,4,5,6],2)

def rotateArr2(arr,d):
    newList = arr[d:]+arr[0:d]
    print(newList)
rotateArr2([1,2,3,4,5,6,7],2)