
def merge(left,right):
    global cnt
    sorted=[]
    i,j=0,0
    while(i<len(left) and j<len(right)):
        if left[i]<=right[j]:
            sorted+=[left[i]]
            i+=1
        else:
            sorted+=[right[j]]
            j+=1
            cnt+=len(left)-i
        
    if i>=len(left):
        sorted+=right[j:len(right)]
    if j>=len(right):
        sorted+=left[i:len(left)]

    return sorted
    
def merge_sort(unsorted_list):
    n=len(unsorted_list)

    if n<=1:
        return unsorted_list

    mid=int(n/2)
    left=unsorted_list[0:mid]
    right=unsorted_list[mid:n]

    # print(left,right)

    sorted_left=merge_sort(left)
    sorted_right=merge_sort(right)
    # print(merge(sorted_left,sorted_right))
    return merge(sorted_left,sorted_right)



def sort_count(unsorted_list):
    global cnt 
    cnt=0
    return merge_sort(unsorted_list)


def test():
   
    # unsorted=[6,5,4,3,2,1]
    unsorted=[]
    with open("C:\\Users\\LYN\\Desktop\\Algorithms\\assignment01\\IntegerArray.txt") as f:
        lines=f.readlines()
 
        for line in lines:
            unsorted.append(int(line.strip('\n')))

    sort_count(unsorted)
    print(cnt)
    # print(merge([4,1],[23,14]))

  
test()
