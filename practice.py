fruit = ["orang","apple","banana","mango"]
new_list = []
for i in fruit:
    if "a" in i:
        new_list.append(i)
print(new_list)
newlist = [z for z in fruit if"a" in z]
print(newlist)

number = [x for x in range(1,10) if x>5 ]
print(number)


frt = ["my favorit" for y in fruit ]
print(frt)

l=fruit.index("banana")
print(l)
print(fruit[2])

def hi(n):
    return "hi! how are you: "+n
l=map(hi,("ali","amir","sajid ali khan"))
list=list(l)
for i in list:
    print(i)

dic = {"name":"Usman","Father_Name":"TariqAzam","Contact":"03048114406"}
list2=dic["name"]
print(list2)