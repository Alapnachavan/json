# import json
# x = '{ "name":"John", "age":30, "city":"New York"}'
# y=json  .loads(x)
# print(y["name"])

# 
# a={'lalalala': 3}

# import json
# dict={
#     "student":{
#         "name":"alpana",
#         "age":"30",
#         "vilage":"saswad"
#     },
#     "student":{
#         "name":"alpana",
#         "age":"20",
#         "vilage":"bhor"
#     }
# }

import json 
x ='{ "name":"John", "age":30, "city":"New York"}'
y=json.loads(x)
print(y["name"])
dict={
    "student":{
        "name":"alpana",
        "age":"30",
        "vilage":"saswad"
    },
    "student":{
        "name":"alpana",
        "age":"20",
        "vilage":"bhor"
    }
}
file=open("new_file interview q.json","w")
json.dump(dict,file,indent=6)
file.close()
# with open("data.json","w") as write_file:  
    # json.dump(dict,write_file)  
  
with open("new_file interview", "r") as read_file:  
    b = json.load(read_file)  
print(b)  
# a={"lalalala": 3}
# x= json.dumps(a)import json
# x = '{ "name":"John", "age":30, "city":"New York"}'
# y=json  .loads(x)
# print(y["name"])
# print(a)







