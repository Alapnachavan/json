import json

shopping_list={
    "shopping_list":
        { 
            "chaco":"15",
            "Biscuits":"50",
            "Diary_milk":"30",
            "ice_cream":"20",
        } 
}
out_file=open("shopping_list.json","w")
json.dump(shopping_list,out_file)
item=input("enter the any items:")
quantity=int(input("enter the quantity:"))
mydict={}
new_shopping_list={}
mydict[item]=quantity
for i in shopping_list:
    for j in shopping_list[i]:
        for k in mydict:
            if j !=k:
                new_shopping_list[j]=shopping_list[i][j]
                if k not in shopping_list[i]:
                    new_shopping_list[k]=mydict[k]
out_file=open("new_shopping_list.json","w")
json.dump(new_shopping_list,out_file)
out_file.close