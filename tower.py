# Online Python compiler (interpreter) to run Python online.
def tower_of_hanoi(n,source,destination,auxilary):
    if n==1:
        print ("move disk 1 from",source,"to",destination)
        return
    tower_of_hanoi(n-1,source,auxilary,destination)
    print("move disk",n,"from",source,"to",destination)
    tower_of_hanoi(n-1,auxilary,destination,source)
n = 5
tower_of_hanoi(n,'a','b','c')