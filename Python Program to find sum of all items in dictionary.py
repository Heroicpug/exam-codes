def returnsum(mydict):
    s = 0
    for i in mydict:
        s =s+mydict[i]
    return s
dict1 = {'a':100,'b':200,'c':300}
print("sum :",returnsum(dict1))
