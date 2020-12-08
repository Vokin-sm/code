total=0
for i in range(1,10):
    total+=i
print(total)    


total2=0
i2=0
while i2<10:
    total2+=i2
    i2+=1
print(total2)    


my_list=[7,5,4,4,3,2,1,-5,-10,-15]
total3=0
i3=0
while my_list[i3]>0:
    total3+=my_list[i3]
    i3+=1
print(total3)    


total4=0
i4=0
for element in my_list:
    if element<=0:
        break
    total4+=element
print(total4)

total5=0
i5=0
while total5<10 and my_list[i5]>0:
    total5+=my_list[i5]
    i5+=1
print(total5)    

my_list=[7,5,4,4,3,2,1,-5,-10,-13,-15,-18]
total6=0
i6=-1
while my_list[i6]<0:
    total6+=my_list[i6]
    i6+=-1
print(total6)

total7=0
for i7 in range(len(my_list)-1,-1,-1):
    if my_list[i7]>0:
        break
    total7+=my_list[i7]
print(total7)




words=["apple","banana","grape","some other word","stop","hello","goodbye"]
i8=0
while words[i8]!="stop":
    print(words[i8])
    i8+=1



for i9 in range(len(words)):
    if words[i9]=="stop":
        break
    print(words[i9])

print ("Hello word")
