def swap(swap_list,i,j):
    swap_list[i],swap_list[j]=swap_list[j],swap_list[i]

def quick_sort(unsorted_list,l,r):
    if r==l:
        return 
    if r-l==1:
        if unsorted_list[l]>unsorted_list[r]:
            swap(unsorted_list,l,r)
        
    pivot=unsorted_list[l]
    i,j=l+1,r

    while i<j:
        if unsorted_list[i]>pivot:
            if unsorted_list[j]<pivot:
                swap(unsorted_list,i,j)
                i+=1
                j-=1
            else:
                j-=1
        else:
            i+=1
    print(i,unsorted_list)
    if unsorted_list[l]>unsorted_list[i]:
        swap(unsorted_list,l,i) 
    quick_sort(unsorted_list,l,i-1)
    quick_sort(unsorted_list,i,r)

    
def sort(unsorted_list):
    n=len(unsorted_list)
    l,r=0,n-1
    return quick_sort(unsorted_list,l,r)

def test():
   
    unsorted=[6,1,10,3,2,5,1]
    sort(unsorted)
    # swap(unsorted,0,5)
    print(unsorted)
    # print(merge([4,1],[23,14]))
 
test()