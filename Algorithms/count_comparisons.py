def swap(swap_list,i,j):
    swap_list[i],swap_list[j]=swap_list[j],swap_list[i]

def quick_sort(unsorted_list,l,r):
    global cmp
    cmp+=(r-l)

    if r==l:
        return 
 
    pivot=unsorted_list[l]
    i=l+1
    for j in range(l+1,r+1):
        if unsorted_list[j]<pivot:
            swap(unsorted_list,i,j)
            i+=1
    # print(i,unsorted_list)
    # if unsorted_list[l]>unsorted_list[i-1]:
    swap(unsorted_list,l,i-1) 

    quick_sort(unsorted_list,l,i-1)
    quick_sort(unsorted_list,i,r)

    
def sort(unsorted_list):
    global cmp
    cmp=0
    n=len(unsorted_list)
    l,r=0,n-1
    return quick_sort(unsorted_list,l,r)

def test():
   
    # unsorted=[9,6,1,10,3,2,5,8,4,7]
    # sort(unsorted)
    # # swap(unsorted,0,5)
    # print(unsorted)
    # print(merge([4,1],[23,14]))
    unsorted=[]
    with open("C:\\Users\\LYN\\Desktop\\Algorithms\\assignment02\\QuickSort.txt") as f:
        lines=f.readlines()
 
        for line in lines:
            unsorted.append(int(line.strip('\n')))
   
    sort(unsorted)
    # print(unsorted)
    print(cmp)

 
test()