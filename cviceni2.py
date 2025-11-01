def my_range (start, stop, step = 1):
    vys = []
    i = start
    while (step > 0 and i < stop):
        vys.append(i)
        i += step
    return vys 

def my_enumerate (seznam, start = 0):
    vys = []
    i = 0 
    while i < len(seznam):
        vys.append((start + i, seznam[i]))
        i+=1
    return vys

if __name__ == "__main__":
    #print(list(range(1,11)))
    #print(list(range(1,11,2)))

    #print("My range")
    #print(my_range(1,10))
    #print(my_range(1,10, 2))

    print(list(enumerate(["a", "b", "c"])))
    print(list(enumerate(["a", "b", "c"], 1)))

    print(list(my_enumerate(["a", "b", "c"])))
    print(list(my_enumerate(["a", "b", "c"], 1)))