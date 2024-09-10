import time
start=time.time()
a=[1,2,3,4]
a.insert(4,5)
print(a)
a.pop(0)
print(a)
size=len(a)
print("length of the list:",size)
end=time.time()
print("run time of the program is:",end-start)
