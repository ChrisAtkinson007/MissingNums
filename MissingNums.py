#Assumptions: Array of integers N, where 0<=N<=20
array1=[0, 1, 2, 8, 12, 13]
array2=[1, 2, 5, 12, 16]

def missingnums(NumArray):
    l1=[]
    #Sort the array in ascending order, and make all values unique using set function
    if len(NumArray)==0:
        return 0
    NumArray=list(set(NumArray))
    NumArray.sort()
    #EdgeCase to check if initial element of array is 0
    if NumArray[0]!=0:
        if (NumArray[0])==1:
            l1.append('0')
        else:
            l1.append(f'0-{NumArray[0]-1}')

    #Iterate through sorted elements and append missing elements as a string to list l1
    for i in range(0,len(NumArray)-1):
        if (NumArray[i+1]-NumArray[i])!=1:
            if (NumArray[i+1]-NumArray[i])==2:
                l1.append(str(NumArray[i]+1))
            else:
                l1.append(f'{NumArray[i]+1}-{NumArray[i+1]-1}')

    #Check if final element of array is 20, if not we add the final missing elements
    if NumArray[-1]!=20:
        if NumArray[-1]==19:
            l1.append('20')
        else:
            l1.append(f'{NumArray[-1]+1}-20')

    l1str=','.join(l1)

    return l1str

print(missingnums(array1))
print(missingnums(array2))
