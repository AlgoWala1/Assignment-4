import random
i,j = 0,0
ans = 0
for k in range(0,10):
    i = random.randint(1,11)
    j = random.randint(1,11)
    print("Question " , k+1,":",i,"*",j,"=")
    ans = int(input("Ans:"))
    if ans == i*j:
        print("Right!")
    else:
        print("Wrong, The answer is ",i*j)
    
    
    
