
def  HalfList(mynumbers):
    list1=[]
    list2=[]
    n=len(mynumbers)
    x=int(n/2)
    print (x)
# Create list1 with half elements (first  elements)
    list1 = mynumbers[:x]
 # Create list2 with next half elements (next  elements)
    list2 = mynumbers[x:]

    for i in range(0, len(list1)):
        list1 = [int(i) for i in list1]
        mytotal = sum(list1)
    return mytotal

def main():
    mynumbers = [0] * 6
    mytotal = int()

    mynumbers = [6, 5, 7, 9, 4, 3,]
    mytotal = HalfList(mynumbers)
    print(mytotal)
main()