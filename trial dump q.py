import json

dict={
    "emp1":{
        "name":"rutuja",
        "age":"20",
        "collage":"saswad"

    },
    "emp2":{
        "name":"alpana",
        "age":"20",
        "collage":"saswad"

    }
}
file=open("myfile.json","w")
json.dump(dict,file,indent=6)
file.close()

