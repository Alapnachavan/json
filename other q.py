import json
list1=["Alpana","Bhor","commers student","wagire collage"]
list2=["Rutuja","saswad","commers student","wagire collage"]
list3=["Srushti","saswad","commers student","wagire collage"]
list4=["gressy","pune","science student","wagire collage"]
list5=["shruti","hadpsar","science student","wagire collage"]
keys=["name","city name","faclty name","collage name"]
student1={}
student2={}
student3={}
student4={}
student5={}
dict1={"student1":student1,"student2":student2,"student3":student3,"student4":student4,"student5":student5}
for i in range(len(list1)):
    student1.update({keys[i]:list1[i]})
for j in range(len(list2)):
    student2.update({keys[j]:list2[j]})
for k in range(len(list3)):
    student3.update({keys[k]:list3[k]})
for a in range(len(list4)):
    student4.update({keys[a]:list4[a]})
for b in range(len(list5)):
    student5.update({keys[b]:list5[b]})
with open("other q.json","w")as g:
    json.dump(dict1,g,indent=2)
girl_name=input("enter the girl name:")
for keys ,value in dict1.items():
    print(value)
    for girl_name in value:
        print(keys+":",keys[value])







