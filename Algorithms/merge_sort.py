
def merge_sort(unsorted_list):
    n=len(unsorted_list)

    if n<=1:
        return unsorted_list

    mid=int(n/2)
    left=unsorted_list[0:mid]
    right=unsorted_list[mid:n]
    sorted_left=[]
    sorted_right=[]
    print(left,right)

    sorted_left+=merge_sort(left)
    sorted_right+=merge_sort(right)
    print(merge(sorted_left,sorted_right))
    return merge(sorted_left,sorted_right)


def merge(left,right):
    sorted=[]
    i,j=0,0
    while(i<len(left) and j<len(right)):
        if left[i]>=right[j]:
            sorted+=[left[i]]
            i+=1
        else:
            sorted+=[right[j]]
            j+=1
        

    if i>=len(left):
        sorted+=right[j:len(right)]
    if j>=len(right):
        sorted+=left[i:len(left)]

    return sorted
    

def sort(unsorted_list):
    return merge_sort(unsorted_list)


def test():
   
    unsorted=[1,4,23,14,63,21,10,29,50]
    print(sort(unsorted))
    # print(merge([4,1],[23,14]))
    
test()
