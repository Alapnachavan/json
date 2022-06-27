import json
from textwrap import indent
dict={
    "student1":{
        "name":"rutuja",
        "age":"30",
        "vilage":"saswad"
    },
    "student2":{
        "name":"alpana",
        "age":"20",
        "vilage":"bhor"
    }
}
# file=open("inteview_file.json","w")
# json.dump(dict,file,indent=6)
# file.close()
# # y=json.loads(dict)
# # print(dict["name"])
# x= json.load(dict)
# print(dict)
file=open("alpana_file.json","w")
json.dump(dict,file ,indent=6)
file.close()

# a=2
# print(type(a))
# a=2+5j
# print(a)
# d="my"
# print("d")

# a=95
# b=75
# print(a+b)
# a=3+7j
# b=7+8j
# print(a+b)


# a="2"
# b=7
# print(a+b)
# a=int(a)
