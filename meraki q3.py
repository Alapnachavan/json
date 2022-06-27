import json
python_obj={
    "name":"alpana",
    "class":"I",
    "age" : 6

}
file=open("que3.json","w")
print(type(python_obj))
j_data=json.dumps(python_obj)
print(j_data)
file.close()