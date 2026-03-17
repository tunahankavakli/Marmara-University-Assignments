for i in range(100,1000):
    birler=int(i%10)
    onlar=int((i/10)%10)
    yuzler=int((i%10)%10)
    if((birler+yuzler)>onlar):
        print(i)