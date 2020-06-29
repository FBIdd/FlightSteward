import random
random.seed(125)
num=random.randint(0,100)
#print(num)
time=0

while True:
    ans=input("Please input:")
    if ans.isdigit()==True:
        if int(ans)>num:
            print("Too big!")
            time=time+1
        elif int(ans)<num:
            print("Too small!")
            time=time+1
        if int(ans)==num:
            time=time+1
            print('%d times,you got it!'%(time))
            break
    else:
        print("Please input integer!")
