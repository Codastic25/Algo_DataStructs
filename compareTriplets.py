def compareTriplets(a, b):
    # Write your code here

    aliceScore = 0
    bobScore = 0
    
    for i in range (len(a)):
        if a[i]>b[i]:
            aliceScore=aliceScore+1
        elif a[i]<b[i]:
            bobScore=bobScore+1
            
    return [aliceScore, bobScore]