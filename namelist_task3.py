name_list = ["alice", "bob" "alex", "brian"]
for data in name_list:
    if "alice" in data:
        data.remove("alice")
        print(name_list)
else:
    name = input("enter new name: ")    
    name_list.append(name)    
    print(name_list)