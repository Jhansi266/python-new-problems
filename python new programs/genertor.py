def my_gen():
    n=1
    print("this is the first")
    yield n #print the output 1

    n+=1
    print("this is the second")
    yield n #output 2

    n+=1
    print("this is the third")
    yield n #output 3
for i in my_gen():
    print(i)


    
